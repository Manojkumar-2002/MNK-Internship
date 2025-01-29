def generate_sublists(lst):
    sublists = []
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists
print("All Sublists:", generate_sublists([1, 2, 3]))