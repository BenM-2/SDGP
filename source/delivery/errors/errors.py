"""
@Author:        George Dawson
@Date:          13/11/2026
@Name:          errors.py
@Description:   This file contains custom error classes for the delivery package. These classes are used to handle specific error scenarios that may arise during the execution of the program.
"""

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


class GenericError(Errors):
    pass