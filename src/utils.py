## saving code in the cloud || common things that we are going to probabily import or use
import os
import sys
import dill ## to save the object in the file pikle(preprocess) file will create

import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object (file_path,obj): ## for save object in the file
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:##open(file_path, "wb") opens the file in write-binary (wb) mode, which is required for saving objects.dill.dump(obj, file_obj) saves the object (obj) into the file.
            dill.dump(obj,file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)