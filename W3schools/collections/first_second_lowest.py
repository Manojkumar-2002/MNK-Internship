students = {}

second_name = ""
first_name = ""
lowest_mark = float("inf")

for i in range(5):
    st_name = input(f"Enter Student {i+1}'s name")
    st_mark = float(input(f"Enter Student{i+1}'s mark"))
    students[st_name] = st_mark
    if students.get(st_name) <= lowest_mark:
        lowest_mark = st_mark
        second_name = first_name
        first_name = st_name

        
print(students)
print("first lowest",first_name, students[first_name])
print("second lowest",second_name, students[second_name])