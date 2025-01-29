import random
import string

alphabets = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
print(alphabets)
print(numbers)
print(symbols)
user_alp = int(input("how many alphabets do you want"))
user_num = int(input("how many digits do you want"))
user_symb = int(input("how many symbols do you want"))
password = ''.join(random.choice(alphabets) for _ in range(user_alp))
password += ''.join(random.choice(numbers) for _ in range(user_num))
password += ''.join(random.choice(symbols) for _ in range(user_symb))
pass1 = ''
for i in password:
    pass1 += "".join(random.choice(password))

print(pass1)