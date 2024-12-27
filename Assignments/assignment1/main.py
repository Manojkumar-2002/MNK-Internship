import os
import csv
from file_exceptions import (
    FileProcessingError,
    FileNotFoundError,
    InvalidFileFormatError,
    EmptyFileError,
    MissingColumnError
)

def process_csv(file_path, required_columns=None):
    required_columns = required_columns or ["name", "age"]
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    if not file_path.endswith(".csv"):
        raise InvalidFileFormatError(file_path)
    if os.stat(file_path).st_size == 0:
        raise EmptyFileError(file_path)
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)
        missing_columns = [col for col in required_columns if col not in reader.fieldnames]
        if missing_columns:
            raise MissingColumnError(missing_columns)
        rows = [row for row in reader]
        if not rows:
            raise EmptyFileError(file_path)
        return rows


def main():
    file_path = "data.csv"
    try:
        required_columns = ["name", "age", "email"]
        rows = process_csv(file_path, required_columns)
        print("CSV file processed successfully!")
        for row in rows:
            print(row)
    except FileProcessingError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
