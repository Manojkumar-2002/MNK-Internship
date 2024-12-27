class RomanToInteger:
    def convert(self, roman):
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_value = 0
        for char in roman[::-1]:
            value = roman_map[char]
            total += value if value >= prev_value else -value
            prev_value = value
        return total

roman_int = RomanToInteger()
print(roman_int.convert("MXCL"))