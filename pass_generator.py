import random

def password_generator(length):
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$*-_'
    password = ''
    for i in range(length):
        password = password + random.choice(characters)
    return password

length = int(input("Enter the length of password:"))
print("Generated password:", password_generator(length))