def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

print("8. Remove duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))