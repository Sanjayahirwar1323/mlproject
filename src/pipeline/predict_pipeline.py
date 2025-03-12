## model created -> predict for new data
import sys 
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):  ## just like model prediction just doing prediction 
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
##The class is responsible for storing and structuring input data from an HTML form. This data is likely used for processing in a Machine Learning model or a database.
class CustomData: ## responsible in mapping all the input data that we are giving in the HTML file (BACKEND)
    def __init__(  self,    ## giving input feature 
        gender: str,        ## It initializes instance variables using values passed as arguments.
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender ## The attributes store values for later use, such as passing the data into a model for prediction or saving it in a database

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score
##This method converts the input attributes of the customData class into a pandas DataFrame. 
    def get_data_as_data_frame(self): ## return all my input in the foam of  data frame || A DataFrame in pandas is a two-dimensional, labeled data structure (like an Excel table) that allows efficient storage, manipulation, and analysis of structured data. 
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

