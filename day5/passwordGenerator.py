print("Welcome to the Password Generator")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level 
# In one by one formate
# 52 letters , 10 numbers , 9 symbols

# let 10 2 4
# first of all select 2 symbols out of 9 randomly 
password = ""
for i in range(1,nr_symbols+1): #it will run 2 time
    password+=(symbols[random.randint(0,8)])
for i in range(1,nr_numbers+1): #it will run 4 times
    password+=(numbers[random.randint(0,9)])
for i in range(1,nr_letters-nr_symbols-nr_numbers+1): #it will run 6 times
    password+=(letters[random.randint(0,9)])

print(password)
# random.shuffle(password)
# print(password)

# Hard 
# order is completely random 
# my logic : if three of them are more then 1 then randomly select one of them and then randomly select it's elements
password = ""
lcount = nr_letters - nr_numbers - nr_symbols
for i in range(1,nr_letters+1):
    if(nr_numbers>0 and nr_symbols>0 and lcount>0):
        choice = random.randint(0,2)
        if(choice==0):
            password+=numbers[random.randint(0,9)]
            nr_numbers -= 1
        elif(choice==1):
            password+=symbols[random.randint(0,8)]
            nr_symbols -= 1
        elif(choice==2): 
            password+=letters[random.randint(0,51)]
            lcount -= 1
    elif(nr_numbers>0 and nr_symbols>0):
        choice = random.randint(0,1)
        if(choice==0):
            password+=numbers[random.randint(0,9)]
            nr_numbers -= 1
        elif(choice==1):
            password+=symbols[random.randint(0,8)]
            nr_symbols -= 1
    elif(nr_symbols>0):
        password+=symbols[random.randint(0,8)]
        nr_symbols -= 1
    elif(nr_numbers>0):
        password+=numbers[random.randint(0,9)]
        nr_numbers -= 1
    else:
        password+=letters[random.randint(0,51)]
        lcount -= 1
# Need improvements here 
print(password)

# random.choice(letters) It will give the random item from the list []


