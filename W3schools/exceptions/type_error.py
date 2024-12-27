try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs must be numerical.")
    result = float(num1) + float(num2)
    print("Sum:", result)
except TypeError as e:
    print("Error:", e)
