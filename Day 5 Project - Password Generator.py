import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passwordlist = [] #Created to store a value using .append

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for char in range(0, nr_letters + 1): #The for loop will repeat equals to how many numbers the user typed.
    passwordlist.append(random.choice(letters)) #This code will randomly choose a character inside
    # the list 'letters' and .append will add these random characters to lhe 'passwordlist'
for char in range(0, nr_symbols + 1):
    passwordlist.append(random.choice(symbols))
for char in range(0,nr_numbers + 1):
    passwordlist.append(random.choice(numbers))

random.shuffle(passwordlist) #The random.shuffle will randomize the passwordlist.

#Then we need to transform the list into a string. First we create a variable only containing strings.
passwordstring = ""

#Then after we will loop for how many characters are in the list 'passwordlist' using for
for char in passwordlist:
    # This code will transfer the 'char' values to 'passwordstring' and we have a list transformed into a string!
    passwordstring += char

print(passwordstring)