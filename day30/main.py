# FileNotFound Error
# with open("file.txt") as file:
#     file.read()

# It will generate an error if the file does not exits
# and it doesn't continue

# Key Error
# a_dict = {"key":"value"}
# value = a_dict["nonkey"]

# Index Error

#Type Error

# Catching Exceptions
# try except else and finally keywords
# try = block of code that might get wrong
# excpet = if there was an exception then do this code
# else = do this if there were no exceptions
# finally = Do this no matter what happens

# try:
#     # pass  # it will call else method not except
#     file = open("a_file.txt")
#     a_dict = {"key":"sjdf"}
#     print(a_dict["nonKey"])
# except FileNotFoundError:
#     # It will ignore all other errors after that first error but it will not catch specific exceptions, so have a multiple exceptions
#     print("There was an error")
#     file = open("a_file.txt", mode="w")
# except KeyError as error_message:
#     print("This is a key error")
#     print(f"{error_message}")
# else:
#     print("all things done successfully")
# finally:
#     file.close()
#     print("finally")
#     # raise KeyError("This is error message ") # to raise a error
#

# height = float(input("Height: "))
# weight = int(input("weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight/height**2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)


# KeyError
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except:
#         pass
#
# print(total_likes)

# Exception handling in Nato phonetic alphabet


# json.dump() == data should be go in as dictionary
# json.dump(new_data, data_file), now open data.json file
# json.dump(new_data, data_file, indent=4) to write data in file

# TO read the json data
# data = json.load(data_file pr path)
# print(data)
# data has a type of dictionary
# So we can serialise and deserialise the data using this two methods

# Now how to update data, as we don't want to uodate , mode = write
# get data using load
# data.update(new_data)

# then dump the data in the file
import json

with open("data.json", mode="w") as file:
    data = {"other":{"email": "ketanrtd1@gmail.com", "password":"1234"}}
    json.dump(data, file, indent=4)

with open("data.json", mode="r") as file:
    data_read = json.load(file)

# See how to update data

