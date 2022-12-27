from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import convert_collection_to_dataframe
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
          convert_collection_to_dataframe("aps","sensor")
     except Exception as e:
          print("I am here")
          print(e)

