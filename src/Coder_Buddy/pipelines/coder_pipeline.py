
from src.Coder_Buddy.components.coder import CoderComponents
import logging
from src.Coder_Buddy.utils.abstract_methods import Pipeline
from utils.asyncHandler import asyncHandler
class CoderPipeline(Pipeline):
    def __init__(self):
        pass
    

    @asyncHandler
    async def initiate(self,topic:str):
        logging.info(f"CoderPipeline started for topic: {topic}")
        result = await CoderComponents().initiate(topic=topic)
        logging.info("CoderPipeline completed successfully.")
        return result