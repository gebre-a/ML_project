import logging
import sys
from src.logs import logging

def handle_exception(error,detail_error:sys):

    """
    Handle the exception and print the error message along with the traceback information.
    args:
        error: The exception object that was raised.
        detail_error: The sys module used to retrieve the traceback information.
    """
    exc_type, exc_value, exc_tb = detail_error.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occured in python script name [{0}] line number [{1}] error messages [{2}]".format(filename, line_number,str(error))
    return error_message


class CustomException(Exception):
    """
    Custom exception class that extends the built-in Exception class.
    This class is used to raise custom exceptions with additional information.
    """

    def __init__(self, error_message, detail_error:sys):
        """
        Initialize the CustomException object with an error message and traceback information.
        args:
            error_message: The error message to be associated with the exception.
            detail_error: The sys module used to retrieve the traceback information.
        """
        super().__init__(error_message)
        self.error_message = handle_exception(error_message, detail_error)
    def __str__(self):
        """
        Return the string representation of the CustomException object.
        This method is called when the exception is printed or converted to a string.
        """
        return self.error_message    

