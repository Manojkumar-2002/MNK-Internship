from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 355
    Antarctica = 672
print(set(Country))
for c in sorted(set(Country),key=lambda country: country.value ):
    print(f"{c.name},{c.value}")
    