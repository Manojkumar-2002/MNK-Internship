def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])


print(reverse_words("The quick brown fox")) 
