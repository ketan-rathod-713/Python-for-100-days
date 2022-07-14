# 14 july

# Functions with outputs

def my_function():
    result = 3*2
    return result
print(my_function())

# Just a return keyword and no other stuff 

def format_name(firstName,lastName):
    return firstName.title()+" "+lastName.title()

print(format_name("ketan","rathod"))

# .title function makes first character of word capitalize str.title()

# return tells the computer that this is the end of the function and also we can have empty keyword 
# Multiple return , inside if blocks and all 
# Early return for special cases 