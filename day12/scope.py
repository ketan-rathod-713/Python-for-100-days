# blocks dont have local scope 

# eg. 

level = 10
if(level<11):
    enemy = 1

print(enemy) # This will not show an error

# But if function is there then it will create a local scope for the variables

# How to modify global variables
enemy = 1
def increaseEnemy():
    global enemy  # to use the global variable it is must to write this
    enemy += 1
    print(f"the enemy is {enemy}")
    
increaseEnemy()
print(f"the enemy is {enemy}")
    
# It is confusing and can cause bug , They will tell you to modify the global variable
# what else can we do 

variable1 = 1

def increaseVariable():
    return variable1 + 1

print(increaseVariable()) # so rather then getting variable and declaring it global is tidious task so rather use a function that just returns , But how it can access global variable return statement only ?????

# For constants : all upper case , 

PI = 3.14
CONST = 23
def justTrying():
    print(PI)
    print(CONST)  # So i can use global constant variable that's nice but other then that i can't change them
    # CONST += 21 error 
    # PI = 34 This will cause an error may be because of the assignment
justTrying()
print(CONST)