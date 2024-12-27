class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student(name="John", age=20, grade="A")
student2 = Student(name="Emily", age=22, grade="B")


print(f"Student1: Name = {student1.name}, Age = {student1.age}, Grade = {student1.grade}")


print(f"Student2: Name = {student2.name}, Age = {student2.age}, Grade = {student2.grade}")
