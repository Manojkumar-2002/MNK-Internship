def find_permutations(lst):
    def permute(current, remaining):
        if not remaining:
            result.append(current)
            return
        for i in range(len(remaining)):
            permute(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    result = []
    permute([], lst)
    return result

print("Permutations:", find_permutations([1, 2, 3]))