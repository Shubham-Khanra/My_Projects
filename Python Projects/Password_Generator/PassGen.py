import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Method (You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well.)

# password = ''
# for char in range(0, nr_letters):
#     password += random.choice(letters)
    
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
    
# print(password)


#-------------------------------------------------*********************************----------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

## Hard Method
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list) #Shuffling the order of the password.
print(password_list)

# Converting the password from List to String
password = ''
for char in password_list:
    password += char

print(f'Your Password is: {password}')