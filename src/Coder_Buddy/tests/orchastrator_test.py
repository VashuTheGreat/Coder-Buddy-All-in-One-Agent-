import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.getcwd())

from logger import *
import logging

from src.Coder_Buddy.pipelines.Orchastrator_pipeline import CoderPipeline

import asyncio


async def main():
    try:
        logging.info("Starting CoderPipeline test...")
        coderpipeline = CoderPipeline()

        logging.debug("Initiating coder pipeline with topic: 'Create a calculator web app Calculator'")
        coderpipeline_output = await coderpipeline.initiate(
            topic="Create a calculator web app Calculator"
        )

        logging.info(f"Result: {coderpipeline_output}")



        # ================== FileWriter Pipeline Test ==================
        from src.Coder_Buddy.pipelines.FileWriter_pipeline import fileWriterPipeline
        logging.info("Starting fileWriterPipeline test...")
        file_writer_pipeline = fileWriterPipeline()
        file_writer_output = await file_writer_pipeline.initiate(
            state=coderpipeline_output
        )
        logging.info(f"fileWriterPipeline Result: {file_writer_output}")
    except Exception as e:
        logging.error(f"Error during CoderPipeline test: {e}")

if __name__ == "__main__":
    asyncio.run(main())