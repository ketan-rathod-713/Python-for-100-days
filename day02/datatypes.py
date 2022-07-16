# already learned about string it is string of characters and we can pull out each character
print("Hello"[0])

# if number not written in double quotes then it will thing it as int not string

# Integer Float Bool and so on 

# len(1234) it will produce an error , this function doesn't like to work with this type of datatype

a = "sstring"

print(type(a))
print(type(123))

# also we can do typeCasting

newStringofInt = str(123)  #converting numbers to string
print(type(newStringofInt))

a =float(123) #converted to float 

float("100.5") # we are converting string to float in this , and so on for others 

# Other mathematical operations
# just like other programming lang.add()
# whenever we dividing things we get float not integer 
#  ** for power like 2**3 which is 8 

print(2**3)

# when more then one operation on same line then rule PEMDAS

# () 
# **
# * / , calculation goes from left to right if both are at same level 
# + -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3)/3 - 3) # now the priority of the bracket is more 