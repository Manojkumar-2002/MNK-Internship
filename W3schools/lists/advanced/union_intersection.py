def union_and_intersection(lst1, lst2):
    union = []
    intersection = []
    seen = set()
    for item in lst1 + lst2:
        if item not in union:
            union.append(item)
    for item in lst1:
        if item in lst2 and item not in seen:
            intersection.append(item)
            seen.add(item)
    return union, intersection

print("7. Union and Intersection:", union_and_intersection([1, 2, 3], [2, 3, 4]))