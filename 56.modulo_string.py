import string
import random

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

password = "123"
valid = False

for i in password:
  if i in string.ascii_letters:
    valid = True

print(valid)

caracteres = string.ascii_letters + string.digits + string.punctuation

print(random.choice(caracteres))

codigo = "".join(random.choice(caracteres) for _ in range(10))

print(codigo)