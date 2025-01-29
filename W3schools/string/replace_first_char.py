def replace_first_char(s):
    if len(s) > 1:
        return s[0] + s[1:].replace(s[0], '$')
    return s

print(replace_first_char('restart'))  # 'resta$t'
