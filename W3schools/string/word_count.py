def count_word_occurrences(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

print(count_word_occurrences('hello world hello universe world'))  
