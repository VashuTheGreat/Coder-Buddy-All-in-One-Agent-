from src.Coder_Buddy.components.fileWriter import FileWriterComponent
import logging
from src.Coder_Buddy.utils.abstract_methods import Pipeline
from utils.asyncHandler import asyncHandler
from src.Coder_Buddy.models.Orchastrator_model import State

class fileWriterPipeline(Pipeline):
    def __init__(self):
        pass
    

    @asyncHandler
    async def initiate(self, state: State):
        logging.info(f"fileWriterPipeline started")
        result = await FileWriterComponent().initiate(state=state)
        logging.info("fileWriterPipeline completed successfully.")
        return result