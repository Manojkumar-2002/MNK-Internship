class IntegerToRoman:
    def convert(self, num):
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = ""
        for value, numeral in roman_map:
            while num >= value:
                result += numeral
                num -= value
        return result

int_roman = IntegerToRoman()
print(int_roman.convert(109))