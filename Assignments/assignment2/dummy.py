class CannotAddTwoPlusTwo(Exception):
    """Custom exception raised when attempting to add 2 + 2."""
    def __init__(self, message="Adding 2 + 2 is not allowed."):
        super().__init__(message)

def add_numbers(a, b):
    if a == 2 and b == 2:
        raise CannotAddTwoPlusTwo()
    return a + b

try:
    result = add_numbers(2, 2)
    print(result)
except CannotAddTwoPlusTwo as e:
    print(e)