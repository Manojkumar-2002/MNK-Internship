class FileProcessingError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FileNotFoundError(FileProcessingError):
    def __init__(self, file_path):
        super().__init__(f"File not found: {file_path}")

class InvalidFileFormatError(FileProcessingError):
    def __init__(self, file_path):
        super().__init__(f"Invalid file format: {file_path}. Expected a .csv file.")

class EmptyFileError(FileProcessingError):
    def __init__(self, file_path):
        super().__init__(f"The file is empty: {file_path}")

class MissingColumnError(FileProcessingError):
    def __init__(self, missing_columns):
        super().__init__(f"Missing required columns: {', '.join(missing_columns)}")
