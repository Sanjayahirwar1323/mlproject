## code related to read the data ||  DIVIDE or split data in train test || it generally means the process of importing or loading data from a source into a system (such as a database, DataFrame, or pipeline).
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass 
## to store input such as where we have to store the train test etc we create another class
from src.component.data_transformation import DataTransformation ## from data transformation file 
from src.component.data_transformation import DataTransformationConfig

@dataclass ##automatically generates special methods like __init__(), __repr__(), and __eq__() ## mainlly used when we have variable
class DataIngestionConfig: ##The DataIngestionConfig class provides a structured way to define and store paths for data ingestion.
    train_data_path:str=os.path.join("artifacts","train.csv") ## to store the path to save the training data set || output will store under artifacts folder || train.csv is file name will save in the path 
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self): ##constructor
        self.ingestion_congif=DataIngestionConfig()## all 3 path will save in ingestion_config
    def initiate_data_ingestion(self): ## method to read the data and split the data in train test
        logging.info("Entered the data ingestion method or component")
        try: ## try block is used to check the error or exception
            df=pd.read_csv('notebook/data/stud.csv') ## read the data from the path
            logging.info("Read the data set as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_path),exist_ok=True) ## create the directory where we have to store the train data

            df.to_csv(self.ingestion_congif.raw_data_path,index=False,header=True) ## save the data in the path
            
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42) ## split the data in train test
            
            train_set.to_csv(self.ingestion_congif.train_data_path,index=False,header=True) ## save the train data in the path
            
            test_set.to_csv(self.ingestion_congif.test_data_path,index=False,header=True) ## save the test data in the path
            
            logging.info("ingestion of data completed")
            return(
                self.ingestion_congif.train_data_path, ## return the path of train data
                self.ingestion_congif.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys) ## if any error occur then it will raise the custom exception

##if __name__=="__main__":
   #obj=DataIngestion() ## create the object of the class
    #obj.initiate_data_ingestion() ## call the method to read the data and split the data in train test

    ## atrifacts folder will create in the current directory where the code is running and the train.csv and test.csv will save in the artifacts folder

if __name__=="__main__": ## 1st combine data ingestion then 2nd step compine data transformation
    obj=DataIngestion() ## create the object of the class
    train_data,test_data=obj.initiate_data_ingestion()
    ## 2nd step
    data_transformation=DataTransformation() ## create the object of the class
    data_transformation.initiate_data_transformation(train_data,test_data) ## call the method to read the data and split the data in train test
