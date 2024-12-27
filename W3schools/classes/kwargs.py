def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}")

student_data(1, student_name="John Doe", student_class="10th Grade")
