from collections import namedtuple
from typing import NamedTuple


DataIngenctionConfig = namedtuple("DataIngenctionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationsConfig",["schema_file_path"])

DataTransformationconfig= namedtuple("DataTransformation", ["add_bedroom_per",
                                                            "transformed_train_dir",
                                                            "transformed_test_dir",
                                                            "preprocessed_object_file_path"])


ModelTrainerConfig= namedtuple ("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

ModelEvalutionConfig = namedtuple("ModelEvalutionConfig",["Model_evalution_file_path","time_stamp"])

ModelPusherConfig= namedtuple("ModelPusherConfig",["export_dir_path"])
TrainingPipelineConfig=namedtuple("TrainingPipelineConfig",["artifact_dir"])