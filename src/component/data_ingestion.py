## code related to read the data ||  DIVIDE or split data in train test
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
## to store input such as where we have to store the train test etc we create another class

@dataclass
class DataIngestionConfig




