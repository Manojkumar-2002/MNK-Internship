from collections import Counter

inp = int(input("How many words do you want to type"))
collect = []

for i in range(inp):
    word = input(f"Enter word {i+1}: ").strip()
    collect.append(word)
word_counts = dict(Counter(collect))
for key,value in word_counts.items():
    print(f"{key} {value}")
