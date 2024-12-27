def student(name, age, grade):
    return f"Student Name: {name}, Age: {age}, Grade: {grade}"

print(student.__code__.co_varnames) 
