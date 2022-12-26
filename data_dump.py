import pymongo
import pandas as pd
import numpy as np
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
Database = "aps"

# Collection  Name
Collection = 'sensor'

#Data-Path
data_link = "/config/workspace/aps_failure_training_set1.csv"

##Data Dump in MongoDB

#In Python, the special variable __name__ holds the name of the current module. 
#When a Python script is run directly, the __name__ variable is set to the string "__main__". 
#This can be used to execute some code only when the script is run directly, 
#but not when it is imported as a module into another script.
if __name__ == "__main__":
    df = pd.read_csv(data_link)
    df.reset_index(drop=True, inplace=True)
    #print(df.shape)

    #Convert DataFrame in JSON
    json_records = list(json.loads(df.T.to_json()).values())
    
    #print(json_records[0])
    #Insert Converted Data (JSON) in MongoDB
    client[Database][Collection].insert_many(json_records)
