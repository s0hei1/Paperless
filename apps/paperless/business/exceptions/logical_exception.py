class LogicalException(Exception):
    message: str

    def __init__(self, message="a logical exception was raised"):
        self.message = message
