import random

print("Welcome to the Password Generator!")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

number = int(input("How many passwords would you like to generate? "))
length = int(input("How many characters should the password contain? "))

def password_generator():
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

for i in range(number): 
    generated_password = password_generator()
    print("Generated password:", generated_password)