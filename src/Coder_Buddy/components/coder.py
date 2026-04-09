
from utils.asyncHandler import asyncHandler
import logging
from src.Coder_Buddy.models.Orchastrator_model import State
from src.Coder_Buddy.graphs.coder.coder_graph import graph
class CoderComponents:
    def __init__(self):
        self.graph=graph
        pass
    

    @asyncHandler
    async def initiate(self,topic:str)->State:
        logging.info(f"Entered in the CoderComponent with topic: '{topic}'")
        logging.debug("Initializing state for graph invocation...")
        
        # Fixed typing for plan and tasks (will update Orchastrator_model.py so it accepts them, or empty logic)
        state=State(
            topic=topic,
            plan=None,
            tasks=None
        )

        logging.info("Invoking graph process. This might take a while...")
        state=await self.graph.ainvoke(state)
        
        logging.info("Exited from the coder components block successfully.")
        logging.debug(f"Final state: {state}")
        return state

        