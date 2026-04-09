
from src.Coder_Buddy.models.Orchastrator_model import State
from src.Coder_Buddy.models.worker_model import WorkerOutputSchema, Worker

from src.Coder_Buddy.prompts import WORKER_AGENT_PROMPT
from utils.asyncHandler import asyncHandler
from langchain_core.messages import SystemMessage, HumanMessage
from src.Coder_Buddy.llm.load_llm import llm
from langsmith import traceable

import logging


# ============================= Worker ===============

@asyncHandler
@traceable(name="Worker",tags=['Creating File and Coding'])
async def worker(state) -> dict:
    task = state.get("current_task") if isinstance(state, dict) else getattr(state, "current_task", None)
    if not task:
        logging.error("current_task not found in state in worker node")
        raise ValueError("current_task not found in state")

    logging.info(f"Worker node started for task: {task.filename} at path: {task.folder_path}")
    logging.debug(f"Task description preview: {task.description[:100]}...")

    logging.debug("Initializing LLM for raw code generation")

    plan = state.get("plan") if isinstance(state, dict) else getattr(state, "plan", "")

    logging.info(f"Invoking LLM to generate code for {task.filename}...")
    worker_output = await llm.ainvoke([
        SystemMessage(content=WORKER_AGENT_PROMPT),
        HumanMessage(
            content=f"Task Description: {task.description}\n"
                    f"File Name: {task.filename}\n"
                    f"File Path: {task.folder_path}\n"
                    f"Overall Plan: {plan}\n\n"
                    f"Please generate the full, completed raw source code for {task.filename} now."
        )
    ])
    
    # Strip any markdown code block formatting if it accidentally added it
    raw_code = worker_output.content.strip()
    if raw_code.startswith("```"):
        lines = raw_code.split("\n")
        if len(lines) > 1:
            if lines[0].startswith("```"): lines = lines[1:]
            if lines[-1].startswith("```"): lines = lines[:-1]
            raw_code = "\n".join(lines).strip()

    logging.info(f"Worker node completed for task: {task.filename}. Generated code length: {len(raw_code)} characters.")
    logging.debug(f"Generated code preview: {raw_code[:50]}...")
    
    return {
        "worker_output": [Worker(
            code=raw_code,
            file_name=task.filename,
            folder_path=task.folder_path
        )]
    }
