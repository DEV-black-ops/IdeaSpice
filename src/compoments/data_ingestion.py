import os
import sys 
from src.exception import customException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionconfig:
    train_data_path:str  =os.path.join('artifacts',"train.csv")
    test_data_path:str  =os.path.join('artifacts',"test.csv")
    raw_data_path:str  =os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('entered the data ingestion methord')
        try:
            df = pd.read_csv('src\data\stud.csv')
            logging.info('Reading data as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path_data_path,index=False,header=True)
            logging.info("train test split initiated")
            
            train_set,test_set = train_test_split(df,train_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index= False,header = True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)
            logging.info("Ingestion of data compleated ")
            return(self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        except Exception as e:
            raise customException(e,sys)

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
