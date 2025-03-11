import sys ## used to manuplate the different part of python || for custom exception
from src.logger import logging
def error_message_detail(error,error_detail:sys): ## message getting, error detail present inside the sys 
    _,_,exc_tb=error_detail.exc_info() ## give 3 but we use last info exctb info  which tell in which file the exception is occur and which line exception is occour and store in the variale in exctb
    file_name=exc_tb.tb_frame.f_code.co_filename ## then we will get file name 
    error_message ="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error) ##<- error message ,## for line number 
    )
    return error_message ##Returns the formatted error message.
 
    

class CustomException (Exception):
    def __init__(self,error_message,error_detail:sys): ##construction 
        super().__init__(error_message) ## inherite from exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):##It overrides __str__ to return a readable error message instead of a generic exception output.
        return self.error_message
   
##if __name__=="__main__": ## TO CHECK EVERY THING IS WORKING FINE OR NOT
    
  #  try:
   #     a=1/0
    #except Exception as e:
     #   logging.info("Divide by zero")
      #  raise CustomException(e,sys)
## output CustomException: Error occured in python script name [/Users/sanjayahirwar/Documents/THIS PC/CELL -Y/PROJECTS/ML/src/exception.py] line number [24] error message [division by zero]
## jo current directory hogi (terminal ka end wali) us ma hi log folder ka under logger create hoga