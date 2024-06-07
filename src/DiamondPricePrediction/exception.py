import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_msg) -> None:
        self.error_msg = error_msg
        _, _, self.tb_info = sys.exc_info()
        if self.tb_info:
            self.file_name = self.tb_info.tb_frame.f_locals["__file__"]
            self.line_no = self.tb_info.tb_lineno

    def __str__(self) -> str:
        if self.tb_info:
            return f"Error Encountered \nFileName: {self.file_name}\n"\
                   f"Line Number: {self.line_no}\n" \
                   f"Error Message: {self.error_msg}"
        else:
            return super().__str__()