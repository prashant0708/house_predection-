
from housing.entity.config_entity import DataIngenctionConfig, DataTransformationconfig, DataValidationConfig, ModelEvalutionConfig, ModelPusherConfig, ModelTrainerConfig , TrainingPipelineConfig\
    

class Configuration:
    def __init__(self)-> None:
        pass
    def get_data_ingestion_config(self) -> DataIngenctionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationconfig:
        pass

    def get_model_trainer_config(self)-> ModelTrainerConfig:
        pass
    def get_model_evalution_config(self)-> ModelEvalutionConfig:
        pass
    def get_model_pusher_config(self)-> ModelPusherConfig:
        pass
    def get_training_pipeline_config(self)-> TrainingPipelineConfig:
        pass
