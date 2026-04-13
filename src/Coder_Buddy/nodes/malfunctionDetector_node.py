from utils.asyncHandler import asyncHandler

import logging


@asyncHandler
async def malfunction_handler_node(state):
    logging.info("Entered in the malfunctionDetector node")
    logging.debug(f"State received at malfunctionDetector node: {state}")
    
    # Write code here
    
    logging.info("Exiting from the malfunctionDetector node")
    return state