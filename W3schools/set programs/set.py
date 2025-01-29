# Create a set
my_set = {1, 2, 3}
print("Create a set:", my_set)

# Iterate over sets
my_set = {1, 2, 3}
print("Iterate over sets:")
for item in my_set:
    print(item)

# Add elements to a set
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
print("Add elements to a set:", my_set)

# Remove items from a set
my_set = {1, 2, 3}
my_set.remove(2)
print("Remove items from a set:", my_set)

# Discard item if present
my_set = {1, 2, 3}
my_set.discard(2)
print("Discard item if present:", my_set)

# Intersection of sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Intersection of sets:", set1 & set2)

# Union of sets
print("Union of sets:", set1 | set2)

# Set difference
print("Set difference:", set1 - set2)

# Symmetric difference
print("Symmetric difference:", set1 ^ set2)

# Subset check
set1 = {1, 2}
set2 = {1, 2, 3}
print("Subset check:", set1 <= set2)

# Shallow copy
set1 = {1, 2, 3}
set_copy = set1.copy()
print("Shallow copy:", set_copy)

# Clear a set
my_set = {1, 2, 3}
my_set.clear()
print("Clear a set:", my_set)

# Frozensets
my_frozenset = frozenset([1, 2, 3])
print("Frozensets:", my_frozenset)

# Max and min values
my_set = {1, 2, 3}
print("Max value:", max(my_set))
print("Min value:", min(my_set))

# Length of a set
print("Length of a set:", len(my_set))

# Check if value is present
print("Check if value 2 is present:", 2 in my_set)

# Disjoint sets check
set1 = {1, 2}
set2 = {3, 4}
print("Disjoint sets check:", set1.isdisjoint(set2))

# Superset check
set1 = {1, 2, 3}
print("Superset check:", set1.issuperset({1, 2}))

# Elements in one set but not another
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Elements in set1 but not set2:", set1 - set2)

# Remove intersection
set1 = {1, 2, 3}
set2 = {2, 3}
set1 -= set2
print("Remove intersection:", set1)

# Unique words and counts
words = ["apple", "banana", "apple", "orange"]
unique_words = set(words)
print("Unique words and counts:", {word: words.count(word) for word in unique_words})

# Pairs with target sum
nums = [1, 2, 3, 4]
target = 5
pairs = {(x, y) for x in nums for y in nums if x + y == target and x < y}
print("Pairs with target sum:", pairs)

# Longest common prefix
strings = ["flower", "flow", "flight"]
prefix = strings[0]
for string in strings[1:]:
    while not string.startswith(prefix):
        prefix = prefix[:-1]
print("Longest common prefix:", prefix)

# Max product of pairs
nums = [1, 10, -5, 4]
max_product = float('-inf')
max_pair = ()
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        product = nums[i] * nums[j]
        if product > max_product:
            max_product = product
            max_pair = (nums[i], nums[j])
print("Pair with max product:", max_pair)

# Missing numbers
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Missing numbers (set1 - set2):", set1 - set2)
print("Missing numbers (set2 - set1):", set2 - set1)

# Group anagrams
strings = ["bat", "tab", "cat", "act"]
anagrams = {}
for word in strings:
    key = tuple(sorted(word))
    anagrams.setdefault(key, []).append(word)
print("Grouped anagrams:", list(anagrams.values()))

# Unique 3-number combinations
nums = [1, 2, 3, 4, 5]
target = 7
combinations = set()
for x in nums:
    for y in nums:
        for z in nums:
            if x + y + z == target and len({x, y, z}) == 3:
                combinations.add(tuple(sorted((x, y, z))))
print("Unique 3-number combinations:", combinations)
