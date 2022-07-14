programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "a loop is action of doing same thing",
}

print(programming_dictionary["Bug"])
# make sure you typed key correctly
# use the correct data type , use key as string or number not only char name

# adding items
programming_dictionary["newKey"] = "This is the new key"
print(programming_dictionary["newKey"])

# start a program with empty dictionary and then add elements in it

# programming_dictionary = {}
# to clear out user's stuff

# edit item in dictionary
programming_dictionary["Bug"] = "updated bug"
print(programming_dictionary["Bug"])

# it just gives the key , It is just like map in c++
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

# Nesting List and Dictionaries

# if we can also put list instead of simple value in dictionary and same for vice versa. Nested inside another data

# e.g.

capitals = {
    "France": "Paris",
    "Germany": "berlin",
}

traverl_log = {
    "France": ["paris", "Lillie", "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}

# We can also nesst list inside list

# Dictionary inside dictionary Nested

traverl_log1 = {
    "France": {"cities_visited": ["usa", "msdj"],
               "total_no_of_visits": 12}
}

# Nesting dictionareis inside the List

# [{

# },
#  {

#  }]
# Another version of travel log
traverl_log = [
    {"country": "France", "cities_visited": [
        "usa", "msdj"], "total_no_of_visits": 12}
]
