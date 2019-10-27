
# This exception is raised when a user is not found
class UserNotFoundException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

class UserExistsException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

# This exception is raised when a missing field is found
class MissingFieldException(Exception):
    def __init__(self, message, errors = None):
        super().__init__(message)
        self.errors = errors


