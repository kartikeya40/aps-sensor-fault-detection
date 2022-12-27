from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
from sensor.components import data_ingestion
import sys,os

def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger")
          result = 3/0
          print(result)
     except Exception as e:
          print("Hello")
          raise SensorException(e,sys)

if __name__ == "__main__":
     try:

          #get_collection_as_dataframe("aps","sensor")
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = data_ingestion.DataIngestion(data_ingestion_config = data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
          print("I am here")
          print(e)

