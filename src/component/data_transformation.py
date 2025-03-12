##  || data transformation ||
import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer ##  useful when handling datasets with both numerical and categorical features.
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer ## used to fill the missing value
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.exception import CustomException
from src.logger import logging
import os ## used to create the directory

from src.utils import save_object ##save the object in the file (UTLIS)

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl") 
    
class DataTransformation:
    def __init__(self):
        self.transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):
        '''
        this function is responsible for data transformation
        ''' 
        try:
            numerical_columns = ["writing_score","reading_score"] ## numerical features"
            categorical_columns = [
                "gender",
                "race_ethnicity", 
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline= Pipeline( ## pipeline run on training data set 
                steps=[
                ("imputer",SimpleImputer(strategy="median")), ## fill the missing value with median
                ("scaler",StandardScaler()), ## standard scaling
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")), ## fill the missing value with most frequent->(mode)
                ("onehot",OneHotEncoder()), ## categorical data->numerical data
                ("scaler",StandardScaler(with_mean=False)), ## GPT CORRECTION
                ]
            )

            logging.info(f"categorical column: {categorical_columns}")
            logging.info(f"numerical column: {numerical_columns}")
        
            preprocessor = ColumnTransformer( ##|JOIN| ##preprocessor applies different preprocessing steps (like scaling for numerical and encoding for categorical) to respective columns in a single transformation step using ColumnTransformer
                [
                ("num_pipeline", num_pipeline, numerical_columns), ## name of the pipeline, pipeline, features
                ("cat_pipeline", cat_pipeline, categorical_columns),
                ]

            )

            return preprocessor

        

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        
        try:
            train_df=pd.read_csv(train_path) ## read the train data
            test_df=pd.read_csv(test_path) ## read the test data

            logging.info("Read the train and test data completed")
            
            logging.info("obtaining the preprocessor object")
            
            preprocessing_obj=self.get_data_transformer_object() ## get the preprocessor object
            
            target_columns=["math_score"] 
            numerical_columns = ["writing_score","reading_score"] 
            input_feature_train_df=train_df.drop(target_columns,axis=1) ## drop the target column from the train data
            target_feature_train_df=train_df[target_columns] ##  This line extracts the target variable(s) (dependent variable) from the test dataset.
            
            input_feature_test_df=test_df.drop(target_columns,axis=1) ## drop the target column from the test data
            target_feature_test_df=test_df[target_columns] ## This line extracts the target variable(s) (dependent variable) from the test dataset.

            logging.info(
                f"Applying preprocessing object on taining data frame and testing data frame"
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df) ## fit the preprocessor object on the train data || fit_transform() is used on training data to learn + apply transformation.
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df) ## transform the test data || transform() is used on test/new data using previously learned parameters. 

            train_arr =np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)## Simply joins the input features (input_feature_test_arr) and the target values (target_feature_test_df) side by side (column-wise) into a single NumPy array.
            ]
            test_arr =np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]
            logging.info("saved preprocessing object")
            save_object(
                file_path=self.transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_obj_file_path ##it holds the ile path where the preprocessor object is saved or should be loaded from.   
            ) 
        except Exception as e:
            raise CustomException(e,sys)
            
        

             
    