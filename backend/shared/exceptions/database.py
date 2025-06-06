class ServiceError(Exception):
    """Base class for service-level errors."""

    pass


class NotFoundError(ServiceError):
    """Raised when a resource is not found."""

    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)


class AlreadyExistsError(ServiceError):
    """Raised when a resource already exists."""

    def __init__(self, message="Resource already exists"):
        self.message = message
        super().__init__(self.message)


class DatabaseError(ServiceError):
    """Raised for generic database errors."""

    def __init__(self, message="Database operation failed"):
        self.message = message
        super().__init__(self.message)
