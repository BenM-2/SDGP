"""
@Author:        George Dawson
@Date:          13/11/2026
@Name:          errors.py
@Description:   This file contains custom error classes for the delivery package. These classes are used to handle specific error scenarios that may arise during the execution of the program.
"""

from enum import Enum, auto

class Errors(Exception):
    def __init__(self, message: str, code: int = 0):
        self.message = message
        self.code = code

        super().__init__(message)


    def __str__(self):
        return f"Error {self.code}: {self.message}" if self.code else self.message


class GUIError(Errors):
    pass


class IOError(Errors):
    pass


class ParsingError(Errors):
    pass


class AlgorithmError(Errors):
    def __init__(
        self,
        error: AlgorithmErrorCode,
        message: str = ""
    ):
        self.error = error
        self.message = message or error.name

        super().__init__(self.message)


class AlgorithmErrorCode(Enum):
    Err_Algorithm_Invalid = auto()
    Err_Algorithm_Failed = auto()
    Err_Algorithm_Timeout = auto()
    Err_Algorithm_NoSolution = auto()

    Err_Graph_Invalid = auto()
    Err_Graph_Empty = auto()
    Err_Graph_Disconnected = auto()
    Err_Graph_NodeNotFound = auto()
    Err_Graph_NoPath = auto()

    Err_Input_Invalid = auto()
    Err_Input_Empty = auto()
    Err_Input_OutOfRange = auto()

    Err_Math_DivisionByZero = auto()
    Err_Math_Overflow = auto()
    Err_Math_DimensionMismatch = auto()

    Err_File_NotFound = auto()


class GenericError(Errors):
    pass

