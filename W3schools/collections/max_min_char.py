from collections import Counter

s = "hello world"
counts = Counter(s)
maximum = max(counts,key=counts.get)
minimum = min(counts,key=counts.get)
print(f"maximum char is {maximum} and its count is {counts[maximum]} \nminimum char is {minimum} and its count is {counts[minimum]}")