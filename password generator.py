## PASSWORD GENERATOR

import random
import string
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
my_password = generate_password(12)
print("Generated password:", my_password)
