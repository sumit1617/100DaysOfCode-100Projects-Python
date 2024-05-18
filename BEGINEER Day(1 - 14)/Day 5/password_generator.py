import random
letters = ['a', 'b', 'c', 'f', 'o', 'p', 'w', 'r','t', 'g', 'l','v', 'h', 'n', 'm', 'e', 'A', 'B', 'Q', 'W', 'R', 'Y', 'U', 'I', 'O', 'S',
            'G', 'H', 'K', 'L', 'Z', 'C', 'V', 'B', 'N', 'M']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '&', '*', '?', '!','%', '^']

print("Welcome to PyPassword Generator!")
letters_input = int(input("How many letters would you like to enter in password?\n"))
number_input = int(input("How many mumbers would you like?\n"))
symbol_input = int(input("How many symbols would you like?\n"))

# Easy Password
# password = ""
# for char in range(1, letters_input+1):
#     password += random.choice(letters)

# for char in range(1, number_input+1):
#     password += random.choice(numbers)

# for char in range(1, symbol_input+1):
#     password += random.choice(symbols)


# print(f"You Password is generated succesfully: {password}")

# Hard Level
password_list = []
for char in range(1, letters_input+1):
    password_list.append(random.choice(letters))

for char in range(1, number_input+1):
    password_list += random.choice(numbers)

for char in range(1, symbol_input+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"You Password is generated succesfully: {password}")
