import pandas as pd 
from sensor.config import mongo_client 
def get_collection_as_dataframe(database_name:str,collection_name:str) ->pd.DataFrame:
    """
    This function returns collection as dataframe
    params:
    database_name=database name
    collection_name=collection name
    ========================================
    return pandas dataframe of a collection

    """
    try:
        logging.info(f'Reading data from database: {database_name} and collection:{collection_name}')
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.INFO(f'Found columns:{df.columns}')
        if 'id' in df.columns:
            df=df.drop('_id',axis=1)
        logging.info(f'ROW and columns in df:{df.shape}')
        return df
    except Exception as e:
        raise SensorException(e,sys)

