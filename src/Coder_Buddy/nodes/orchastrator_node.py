
from src.Coder_Buddy.models.Orchastrator_model import State,OrchestratorModel

from src.Coder_Buddy.prompts import PLANNER_AGENT_PROMPT
from utils.asyncHandler import asyncHandler
from langchain_core.messages import SystemMessage, HumanMessage
from src.Coder_Buddy.llm.load_llm import llm
from langsmith import traceable
from langchain_core.messages import SystemMessage, HumanMessage

import logging


# ============================= Orchastrator ===============

@asyncHandler
@traceable(name="Orchastrator",tags=['Planners'])
async def orchastrator(state:State)->State:
    logging.info("Entered in the Orchastrator Node")
    
    logging.debug("Initializing Orchestrator LLM with structured output")
    llm_=llm.with_structured_output(OrchestratorModel)


    logging.info("Invoking Orchastrator LLM...")
    orchastrator_output=await llm_.ainvoke([
        SystemMessage(content=PLANNER_AGENT_PROMPT),
        HumanMessage(content=f"Please create a comprehensive plan and break it down into file-level tasks for the following request:\n{state.topic}")
    ])
    
    logging.debug(f"Orchastrator output generated tasks count: {len(orchastrator_output.tasks) if orchastrator_output.tasks else 0}")
    
    state.plan=orchastrator_output.plan
    state.tasks=orchastrator_output.tasks
    
    logging.info(f"Exiting from the orchastrator node. Plan created with {len(state.tasks) if state.tasks else 0} tasks.")

    return state

