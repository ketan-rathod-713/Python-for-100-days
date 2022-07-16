# if condition 
#     do this 
# else 
#     do this

from operator import truediv


height = int(input("Enter the height in cm ? : "))

if height >= 120:  # just like switch cases 
    print("you can ride")   # Python requires indentation and if not then indentation error 
elif height<=20:
    print("you are child")
elif height<=15:
    print("you are really a child")
else:
    print("you can't ride")
    
# Nested if else conditions 

if height>=20 or height<=10:       #using logical operators and , or and not
    print("you can get free icecreame ha ha")
true = 20   
if true:
    print("just")