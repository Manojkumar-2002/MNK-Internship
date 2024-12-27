# Create a tuple
t1 = (1, 2, 3)
print("Create a tuple:", t1)

# Create a tuple with different data types
t2 = (1, "hello", 3.14, True)
print("Tuple with different data types:", t2)

# Create a tuple of numbers and print one item
t3 = (10, 20, 30)
print("Print one item from a tuple:", t3[1])

# Unpack a tuple into several variables
a, b, c = t3
print("Unpack a tuple:", a, b, c)

# Add an item to a tuple
t4 = t3 + (40,)
print("Add an item to a tuple:", t4)

# Convert a tuple to a string
t5 = ('h', 'e', 'l', 'l', 'o')
print("Tuple to string:", ''.join(t5))

# Get the 4th element from the last element of a tuple
t6 = (1, 2, 3, 4, 5, 6, 7)
print("4th element from last:", t6[-4])

# Create the slice of a tuple
print("Slice of a tuple:", t6[2:5])

# Find repeated items in a tuple
t7 = (1, 2, 3, 1, 4, 1)
repeated = [x for x in t7 if t7.count(x) > 1]
print("Repeated items:", set(repeated))

# Check whether an element exists within a tuple
print("Element exists:", 3 in t7)

# Convert a list to a tuple
lst = [1, 2, 3]
t8 = tuple(lst)
print("List to tuple:", t8)

# Remove an item from a tuple
t9 = (1, 2, 3)
t10 = tuple(x for x in t9 if x != 2)
print("Remove item from tuple:", t10)

# Slice a tuple
print("Slice a tuple:", t9[1:])

# Find the index of an item in a tuple
print("Index of item:", t9.index(2))

# Find the length of a tuple
print("Length of tuple:", len(t9))

# Convert a tuple to a dictionary
t11 = (('a', 1), ('b', 2))
print("Tuple to dictionary:", dict(t11))

# Unzip a list of tuples into individual lists
lst_tuples = [(1, 2), (3, 4), (5, 6)]
lst1, lst2 = zip(*lst_tuples)
print("Unzipped lists:", lst1, lst2)

# Reverse a tuple
print("Reverse tuple:", t9[::-1])

# Convert a list of tuples into a dictionary
lst_tuples2 = [('a', 1), ('b', 2)]
print("List of tuples to dictionary:", dict(lst_tuples2))

# Print a tuple with string formatting
t12 = (100, 200, 300)
print(f"Tuple with formatting: This is a tuple {t12}")

# Replace the last value of tuples in a list
lst_tuples3 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
lst_tuples3 = [t[:-1] + (100,) for t in lst_tuples3]
print("Replace last value:", lst_tuples3)

# Remove empty tuples from a list
lst_tuples4 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Remove empty tuples:", [t for t in lst_tuples4 if t])

# Sort a tuple by its float element
data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
data.sort(key=lambda x: float(x[1]), reverse=True)
print("Sorted tuple by float:", data)

# Count elements in a list until a tuple is found
lst_mix = [1, 2, (3, 4), 5]
count = sum(1 for x in lst_mix if not isinstance(x, tuple))
print("Count until tuple:", count)

# Convert a string to a tuple
s = "python 3.0"
print("String to tuple:", tuple(s))

# Calculate product of tuple numbers
t13 = (4, 3, 2, 2, -1, 18)
product = 1
for x in t13:
    product *= x
print("Product of tuple numbers:", product)

# Average value of tuples
t14 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
average = [sum(x) / len(x) for x in zip(*t14)]
print("Average values:", average)

# Convert tuple of string to integers
t15 = (('333', '33'), ('1416', '55'))
t16 = tuple(tuple(int(n) for n in x) for x in t15)
print("String to integer tuple:", t16)

# Convert tuple of integers to a single integer
t17 = (1, 2, 3)
num = int(''.join(str(x) for x in t17))
print("Tuple to integer:", num)

# Check if element exists in tuple of tuples
t18 = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
exists = any('White' in x for x in t18)
print("Element exists in tuple of tuples:", exists)

# Compute element-wise sum of tuples
t19 = (1, 2, 3, 4)
t20 = (3, 5, 2, 1)
t21 = (2, 2, 3, 1)
element_sum = tuple(sum(x) for x in zip(t19, t20, t21))
print("Element-wise sum:", element_sum)

# Sum of elements in each tuple in a list
lst_tuples5 = [(1, 2), (2, 3), (3, 4)]
sums = [sum(x) for x in lst_tuples5]
print("Sum of elements in each tuple:", sums)

# Convert list of tuples to list of lists
lst_tuples6 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
lst_lists = [list(x) for x in lst_tuples6]
print("List of tuples to list of lists:", lst_lists)
