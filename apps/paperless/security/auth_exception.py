class AuthException(Exception):
    message: str

    def __init__(self, message="Auth Exception"):
        self.message = message

