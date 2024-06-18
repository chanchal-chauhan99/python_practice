import os
import random
import string
import secrets

password_length = 10

print(secrets.token_urlsafe(password_length))

chars = string.ascii_letters + string.digits + string.punctuation +'!@#$%^&*()'

# Generating a random password of specified length
password = ''.join(random.choice(chars) for i in range(password_length))
#print(password)
print("The random password is " + "".join(password))
