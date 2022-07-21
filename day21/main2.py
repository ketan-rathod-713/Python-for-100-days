

# slicing , if want small section of list

# piano_keys[2:5] , position from 2 to 5 ==> get 2 , 3, 4

piano_keys = ["a","b","c","d","e","f"]
print(piano_keys[2:4])
piano_keys[:5] # get all the items till 4

# we can also specify the third argument skip
piano_keys[2:5:2] # so here i will get 2 then 4 not 3

piano_keys[::2] # if i want every second item

piano_keys[::-1] # it reverses the list ???

# This slicing method also works for tuples

piano_tuple = ("a","b","c")

piano_tuple[::2] # and so on
