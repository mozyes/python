# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
password_length = int(input("How many letters would you like in your password?\n"))
symbol_length = int(input("How many symbols would you like?\n"))
number_length = int(input("How many numbers would you like?\n"))

new_password = ""
randomnumber = 0
for n in range (0, password_length):
    if n < symbol_length:
        randomnumber = random.randint(0, len(symbols)-1)
        new_password = new_password + symbols[randomnumber]
    elif n < number_length:
        randomnumber = random.randint(0, len(numbers)-1)
        new_password = new_password + numbers[randomnumber]
    else:
        randomnumber = random.randint(0, len(letters)-1)
        new_password = new_password + letters[randomnumber]
print(f"Here us your password: {new_password}")
