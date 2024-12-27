class FileProcessingError(Exception):
    pass

class FileNotFoundError(FileProcessingError):
    def __init__(self, file_path):
        super().__init__(f"File not found: {file_path}")

class DuplicateUsernameError(FileProcessingError):
    def __init__(self, username):
        super().__init__(f"Username '{username}' already exists.")

class MissingFieldError(FileProcessingError):
    def __init__(self):
        super().__init__("All fields must be filled.")

class UserNotFoundError(FileProcessingError):
    def __init__(self, user_id):
        super().__init__(f"User with ID {user_id} not found.")

class NoDataFoundError(FileProcessingError):
    def __init__(self):
        super().__init__(f"No Data Found")
