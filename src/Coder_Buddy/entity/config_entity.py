from dataclasses import dataclass


from dataclasses import dataclass
from src.Coder_Buddy.constants import *
import os
from datetime import datetime
from typing import List
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, pipeline_name,TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config:TrainingPipelineConfig=TrainingPipelineConfig()
@dataclass
class DataIngestionConfig:
    prompt:List
    html_file_path: str
    css_file_path: str
    js_file_path:str

# @dataclass
# class DataValidationConfig:
#     data_validation_dir:str=os.path.join(training_pipeline_config.artifact_dir,DATA_VALIDATION_DIR_NAME)
#     validation_report_file_path:str=os.path.join(data_validation_dir,DATA_VALIDATION_REPORT_FILE_NAME)


# @dataclass
# class DataTransformationConfig:
#     data_transformation_dir:str=os.path.join(training_pipeline_config.artifact_dir,DATA_TRANSFORMATION_DIR)
#     transformed_train_file_path:str=os.path.join(data_transformation_dir,TRANSFORMED_TRAIN_FILE_PATH)
#     transformed_test_file_path:str=os.path.join(data_transformation_dir,TRANSFORMED_TEST_FILE_PATH)
#     transformed_object_file_path:str=os.path.join(data_transformation_dir,TRANSFORMED_OBJECT_FILE_PATH)


 
# @dataclass
# class ModelTrainerConfig:
#     model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
#     trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILE_NAME)
#     expected_accuracy: float = MODEL_TRAINER_EXPECTED_SCORE
#     model_config_file_path: str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
#     n_estimators = MODEL_TRAINER_N_ESTIMATORS
#     min_samples_split = MODEL_TRAINER_MIN_SAMPLES_SPLIT
#     min_samples_leaf = MODEL_TRAINER_MIN_SAMPLES_LEAF
#     max_depth = MIN_SAMPLES_SPLIT_MAX_DEPTH
#     criterion = MIN_SAMPLES_SPLIT_CRITERION
#     random_state = MIN_SAMPLES_SPLIT_RANDOM_STATE