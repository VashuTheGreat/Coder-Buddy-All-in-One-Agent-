

from utils.asyncHandler import asyncHandler
import logging
from src.Coder_Buddy.models.Orchastrator_model import State
from src.Coder_Buddy.graphs.fileWriter.fileWriter_graph import graph
class FileWriterComponent:
    def __init__(self):
        self.graph=graph
        
    @asyncHandler
    async def initiate(self,state:State)->State:
        logging.info(f"Entered in the FileWriterComponent")
        logging.debug("Initializing state for graph invocation...")
        
        

        logging.info("Invoking graph process. This might take a while...")
        state=await self.graph.ainvoke(state)
        
        logging.info("Exited from the FileWriterComponent block successfully.")
        logging.debug(f"Final state: {state}")
        return state