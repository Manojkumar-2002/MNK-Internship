def calculate_love_score(name1, name2):
    name1 = name1.lower()
    print(name1)
    name2 = name2.lower()
    print(name2)
    letter1 = ['t', 'r', 'u', 'e']
    letter2 = ['l', 'o', 'v', 'e']
    out1 = 0
    out2 = 0
    for i in name1:
        if i in letter1:
            out1 += 1
        if i in letter2:
            out2 += 1
    for i in name2:
        if i in letter1:
            out1 += 1
        if i in letter2:
            out2 += 1
    print(f"{out1}{out2}")


calculate_love_score("varshita", "Kardashian")