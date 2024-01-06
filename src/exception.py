import sys #can be used to get the type, value, and traceback of the exception
from src.logger import logging #logger is for the purpose of logging all the information about the execution
import logging
def error_message_detail(error,error_detail:sys):
    '''
    This function returns the error message and error details
    '''
    _,_,exc_tb=error_detail.exc_info() #exc_info() returns a tuple of type, value, and traceback
    file_name = exc_tb.tb_frame.f_code.co_filename#tb_frame is used to get the frame object from the traceback object
    error_message = "Error Ocurred in python script name[{0}] line number[{1} error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)) #tb_lineno is used to get the line number where the error occured

    return error_message
    
class customException(Exception):
    def __init__(self,error_message,error_detail:sys):#error_detail:sys is used to get the type, value, and traceback of the exception
        super().__init__(error_message)#super() is used to call the parent class constructor
        self.error_message = error_message_detail(error_message,error_detail=error_detail)#error_message_detail() is used to get the error message and error details

    def __str__(self):#__str__() is used to return the error message
        return self.error_message #return the error message
    
