import sys,os

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() #This helps in getting the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message



class SensorException(Exception):

    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message #This prints the error messages


#Way to call the exception file

#if __name__ == "__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        raise SensorException(error_message = e,error_detail=sys)