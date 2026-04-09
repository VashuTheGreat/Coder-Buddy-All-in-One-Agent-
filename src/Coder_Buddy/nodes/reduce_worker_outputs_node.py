
from src.Coder_Buddy.models.Orchastrator_model import State
from src.Coder_Buddy.models.worker_model import WorkerOutputSchema, Worker

from src.Coder_Buddy.prompts import WORKER_AGENT_PROMPT
from utils.asyncHandler import asyncHandler
from langchain_core.messages import SystemMessage
from src.Coder_Buddy.llm.load_llm import llm
from langsmith import traceable

import logging


# ============================= Reduce Worker Outputs ===============

@asyncHandler
@traceable(name="Reduce Worker Outputs",tags=['Creating File and Coding'])
async def reduce_worker_outputs(state: State) -> State:
    logging.info("Entered Reduce Worker Outputs node.")
    
    worker_outputs = state.worker_output if hasattr(state, 'worker_output') else state.get("worker_output", [])
    logging.debug(f"Reducing {len(worker_outputs)} total worker outputs...")
    
    logging.info("Exiting Reduce Worker Outputs node successfully.")
    return {
        "worker_outputs": worker_outputs
    }