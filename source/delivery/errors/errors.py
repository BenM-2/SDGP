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