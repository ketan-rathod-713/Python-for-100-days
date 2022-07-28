
# How it is different when writting turtle's write function and Label pack function **kw

# Advance python arguements
# we know about keyword argument

# arguments with default values
#
# def myFun(a=1, b=2, c=3):
#     print(a+b+c)
#
# myFun()

# They are optional arguements , there are some required arguements

# *args many positional arguements
# Functions that can take any number of arguements

# def add(n1,n2):
#     return n1+n2

# what if i want to allow any number of arguements

def add(*args):
    # Here args is tuple
    print(args)
    # This is the positional arguements, as we refer arguements by position
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,10,20))

# great feature is it present in c++ or java

# **kwargs Many keyworded arguements

def calculate(n,**kwargs):
    print(kwargs)
    # It is a dictionary , it represents keyword arguements
    for key, value in kwargs.items():
        print(key)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=5)

# They took all of the optional arguements and added into the **kwargs

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
# benefit of the get is that if key is not presenet in dictionary then it will return none


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)

