from enum import Enum

class CountryCurrency(Enum):
    USA = ("USA", "USD")
    Canada = ("Canada", "CAD")
    UK = ("UK", "GBP")
    India = ("India", "INR")

    def __init__(self, country, currency):
        self.country = country
        self.currency = currency

for country in CountryCurrency:
    print(f"{country.country} uses {country.currency}")
