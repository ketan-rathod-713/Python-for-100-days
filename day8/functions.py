# caeser cypher program encryption
# 14 july
# function with arguments
def greet(name):
    print(f"hello {name}")
    
greet("ketan")

# what is the difference between arguments and parameters
# parameter is the variable name of the data and argument is the actual data that we are passing

# For more than one input
def greet_with(name,location):
    print(f"hello {name} \nwhat is it like in {location}")
    
greet_with("ketan","surat")   

# positional arguments , this are as we see the order of the parameters

# if we switch the order of the arguments then unexpected can happen 

# what if you want to be more clear then 
# keyword arguments

greet_with(name="ketan",location="surat") # THis time order doesn't matter 

