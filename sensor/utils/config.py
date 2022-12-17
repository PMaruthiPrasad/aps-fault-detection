import pymongo
import pandas as pd
import json
from dataclasses import dataclass 
import os 
@dataclass 
class EnvironmentVariable:
    mongo_db_url:str=os.getenv("MONGO_DB_URL")

env_var=EnvironmentVariable()
mongo_client=pymongo_MongoClient(env_var.mongo_db_url)

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"