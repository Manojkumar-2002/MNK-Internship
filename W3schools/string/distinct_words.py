def sort_distinct_words():
    words = input("Enter comma-separated words: ").split(',')
    print(set(words))
    distinct_words = sorted(set(words))
    print(','.join(distinct_words))

sort_distinct_words()
