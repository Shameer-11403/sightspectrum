import string
import secrets
symbols = ['*','/','@']
password =""
for i in range(8):
    password += secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.digits)
password += secrets.choice(symbols)
print(password)