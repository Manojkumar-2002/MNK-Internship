from collections import deque


dq_object = deque()


num = int(input("how many numbers do you want to enter: "))

for i in range(num):
    dq_object.append(float(input(f"Enter number {i+1}: ")))
print(dq_object)
dq_object.rotate(1)
print("After rotation")
print(dq_object)