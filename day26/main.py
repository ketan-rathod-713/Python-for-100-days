# Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu.
# Nato phenatic alph model

# List comprehension , it cut downs the amount of code

# Create new list from prev. list
# until now make empty list and then for loop and append

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]  # first expression for item in list
print(new_list)

# Here we can do any operation with the item

# We can also work with the string

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

# list range string tuple all are sequences that we can iterate through

numbers = [n*2 for n in range(1, 5)]
print(numbers)

# Conditional list comprehension , one new keyword , if condition

names = ["Alex", "Beth", "Caroline", "Dave", "Elaner", "Freddie" ]

# i only want short names

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_name = [name.upper() for name in names if len(name) >= 5]
print(long_name)


# squared number

nums = [1,3,5,8,9]
squared_num = [n**2 for n in nums]
print(squared_num)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [n for n in numbers if n%2==0]
print(result)

# find the common numbers in file1 and file2

import pandas

with open("file1.txt") as file1:
    data_file1 = file1.readlines()

with open("file2.txt") as file2:
    data_file2 = file2.readlines()

# first enter all data of file1 in result then check if file2 has any different numbers then add that
result = []
for num in data_file1:
    if data_file2.__contains__(num):
        num = num.strip()
        result.append(num)

# shortcut
# result = [int(num for num in data_file1 if num in data_file2)]

print(result)
with open("result.txt",mode="a") as file:
    for num in result:
        file.write(num)

# In us states game the code was too long so decrease it

# missing_states = [state for state in all_states if state not in guessed_states]

# we can also do comprehension with dictionary