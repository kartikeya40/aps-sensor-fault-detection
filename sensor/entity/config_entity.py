from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime
import sys,os

file_name = "sensor.csv"
train_file_name = "train.csv"
test_file_name = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        #Artifact Directory for the output
        self.artifact_dir = os.path.join(os.getcwd(),"artifact", datetime.now().strftime('%d%m%Y-%H%M%S'))

class DataIngestionConfig: 
    
    def __init__(self):
        try:
            self.database_name = "aps"
            self.collection_name = "sensor"
            logging.info("Calling the TrainingPipelineConfig Class")
            self.training_pipeline_config = TrainingPipelineConfig()
            logging.info("Creating Path for data_ingestion, feature_store, train_file and test_file")
            self.data_ingestion_path = os.path.join(self.training_pipeline_config.artifact_dir, "data_ingestion")
            self.feature_store_path = os.path.join(self.data_ingestion_path, "feature_store")
            self.train_file_path = os.path.join(self.data_ingestion_path, "dataset", train_file_name)
            self.test_file_path = os.path.join(self.data_ingestion_path, "dataset", test_file_name)
            self.test_size = 0.2
        except Exception as e:
            raise SensorException(e, sys)
    
    def to_dict(self) ->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)


class DataValidationConfig: ...
class DataTransformationConfig: ...
class ModelTrainerConfig: ...
class ModelEvaluationConfig: ...
class ModelPusherConfig: ...