import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("Welcome to Pypassword generator")

num_letters = int(input("How many letters do you want in the password?"))
num_numbers = int(input("How many numbers do you want in the password?"))
num_symbols= int(input("How many symbols do you want in the password?"))

password = []
for i in range (1, num_letters+1):
    password.append(random.choice(letters))
    
for i in range (1, num_numbers +1):
    password.append(random.choice(numbers))
    
for i in range (1, num_symbols + 1):
    password.append(random.choice(symbols))
    
random.shuffle(password)
new_pass = ""
for i in password:
    new_pass += i

print("Here is your generated password: ",new_pass)