from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import convert_collection_to_dataframe
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
          DataIngestionConfig_1 = config_entity.DataIngestionConfig()
          #print(DataIngestionConfig_1.to_dict())
          data_ingestion_1 = data_ingestion.DataIngestion(data_ingestion_config = DataIngestionConfig_1)
          print(data_ingestion_1.initiate_data_ingestion())

     except Exception as e:
          print("I am here")
          print(e)

