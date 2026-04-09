import os
import shutil
from utils.asyncHandler import asyncHandler
import logging
from src.Coder_Buddy.models.Orchastrator_model import State
from src.Coder_Buddy.constants import PUBLIC_FOLDR_PATH
@asyncHandler
async def create_files(state:State):
    logging.info("Creating files based on worker outputs...")
    for worker_output in state.worker_output:
        logging.debug(f"Processing worker output for file: {worker_output.file_name} at path: {os.path.join(PUBLIC_FOLDR_PATH, worker_output.folder_path)}")
        file_path = os.path.join(os.path.join(PUBLIC_FOLDR_PATH, worker_output.folder_path), worker_output.file_name)
        os.makedirs(os.path.join(PUBLIC_FOLDR_PATH, worker_output.folder_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(worker_output.code)
    logging.info("All files created successfully.")        
    return state