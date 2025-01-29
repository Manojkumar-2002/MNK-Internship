import math
from datetime import datetime


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))



class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Division by zero is not allowed"




class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())



class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        self.accounts[account_number] = initial_balance

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number] >= amount:
            self.accounts[account_number] -= amount

    def get_balance(self, account_number):
        return self.accounts.get(account_number, "Account not found")


circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

person = Person("John Doe", "USA", "1990-05-15")
print("Person's Age:", person.age())

calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))

cart = ShoppingCart()
cart.add_item("Apple", 10)
print("Total Price:", cart.total_price())


bank = Bank()
bank.create_account("12345", 1000)
bank.deposit("12345", 500)
print("Account Balance:", bank.get_balance("12345"))
