# fruits = [item1 , item2] 
# This is a list in python 

from os import stat


states = ["california","LosAngeles"]
print(states[0])
print(states)

# why list start from 0
# we can think it as the offset from the left , The first item is at 0 position and second and so on
states[0] = "Los Angeles"
print(states[-1])
print(states[0])
# Both are not equal
# It counts from the last wow

states.append("Another states")  # TO add one item at a time
states.extend(["another","onece more"]) # TO add more items
print(states)

# Index out of range error

print(len(states))

# Nested lists
fruits = ["apple","orange"]
vegetables = ["coriender","cabbage"]
food = [fruits,vegetables]
print(food)
