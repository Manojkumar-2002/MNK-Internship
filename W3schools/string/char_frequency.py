def count_char_frequency(s):
    return {char: s.count(char) for char in set(s)}

sample_string = 'google.com'
result = count_char_frequency(sample_string)
print(result)
