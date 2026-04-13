
from utils.asyncHandler import asyncHandler
import logging




@asyncHandler
async def coder_node(state):
    logging.info("Entered in the coder node")
    logging.debug(f"State received at coder node: {state}")
    
    # Write code here
    
    logging.info("Exiting from the coder node")
    return state