"""
Please place files here to add operations for use with client protocols.
The name of the file will be used as the namespace and any contained public functions will be used as
operations. The information is passed as kwargs to the function.
Requests which don't match your function defination will return an error.
"""

NS = "" # necessary in this directory.

class OperationError(RuntimeError):
    """
    An exception thrown when something gets wrong during the execution
    of an operation
    """
    def __init__(self, error_code, method, keys):
        self.error_code = error_code
        self.method = method
        self.keys = keys
