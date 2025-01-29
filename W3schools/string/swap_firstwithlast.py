def swap_first_last_char(s):
    if len(s) > 1:
        return s[-1] + s[1:-1] + s[0]
    return s

print(swap_first_last_char('hello')) 
