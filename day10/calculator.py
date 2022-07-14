# Calculator

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

# Make a dictionary in which keys are symbols and values are functions

# Here we have added functions as value in the dictiory 
operations = {
    "+" : add,
    "-" : substract,
    "*":multiply,
    "/":divide
}

# How we will be able to use it , for e.g.

function = operations["+"]
print(function(2,3))

num1 = int(input("what is the first number "))
num2 = int(input("what is the second number "))
for i in operations:
    print(i)
opn = input("which operation you want to do ")
opnfunction = operations[opn]
print(type(opnfunction)) # class function
print(opnfunction(num1,num2))
# add while loop to achieve a continued calculation
# type y if want to continue the calculation with the ans 
# Recursion == calls itself 
# I can put functions name in dictionary and then i can use accordingly by using it's name

# difference between print and return --- \/