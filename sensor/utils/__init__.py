import pandas as pd 
from sensor.config import client
from sensor.logger import logging
from sensor.exception import SensorException 
import os,sys

def convert_collection_to_dataframe(database_name: str, collection_name: str) -> pd.DataFrame:
    #Get the Database and Collection Name, and convert to pandas dataframe

    try:
        logging.info(f"Reading the MongoDB Table from dataframe : {database_name} and Collection : {collection_name}")
        df = pd.DataFrame(list(client[database_name][collection_name].find()))
        logging.info(f"Shape of the Dataframe before dropping duplicates : {df.shape}")
        if "_id" in df.columns:
            df.drop("_id",axis="columns",inplace=True)
        df.drop_duplicates(inplace=True)
        logging.info(f"Columns in the dataFrame after dropping duplicates : {df.columns}")
        logging.info(f"Shape of the Dataframe after dropping duplicates : {df.shape}")
    except Exception as e:
        raise SensorException(e,sys)