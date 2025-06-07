class AuthError(Exception):
    """Base class for authentication errors."""

    pass


class IncorrectPassword(AuthError):
    """Raised when user entered password is not correct."""

    def __init__(self, message="Incorrect user password."):
        self.message = message
        super().__init__(self.message)
