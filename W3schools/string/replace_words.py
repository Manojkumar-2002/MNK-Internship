def replace_not_poor(s):
    if 'not' in s and 'poor' in s and s.index('not') < s.index('poor'):
        s = s.replace(s[s.index('not'):s.index('poor') + 4], 'good')
    return s

print(replace_not_poor('The lyrics is not that poor!'))  
print(replace_not_poor('The lyrics is poor!')) 
