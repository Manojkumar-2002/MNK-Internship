from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for c in sorted(Country,key=lambda country: country.value):
    print(f"{c.name},{c.value}")
    
