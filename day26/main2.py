
# Dictionary comprehension also exists

# new_dict = {new_key:new_value for item in list}

# One step further
# we can make a dictionary based on the existing dictionary

# new_dict = {new_key:new_value for (key,value) in dict.items()}

# For one step further we can also add condition at the end with if
import random

import pandas

names = ["alex","just","caroline","studentName"]

# student_score= {
#     "alex":89 # generate random score for each
# }

student_score = {student:random.randint(1,100) for student in names}
print(student_score)

# now loop through the dictionary

passed_students = {student:score for (student, score) in student_score.items() if score>=50}
print(passed_students)

# Challenge 1 Make a dictionary from this with key each word and value be it's length
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()

result_dict1 = {word:len(word) for word in word_list}
print(result_dict1)

# Challenge 2 , Convert dictionary to new dictionary with ferenhit values
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c*9/5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# How to use loops with pandas dataFrame and how to iterate over pandas' data frame

# for looping dictionary
# for (key,value) in dict.items():
#     print(key)

# For dataFrame it's much like dictionary
student_dict = {
    "student":["angela","James","Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

# Loop through a data frame

# for (key,value) in student_data_frame.items():
#     print(key)
#     print(value)

# it loops through each column but that is not usefull so pandas have inbuilt

# Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    # print(index)
    print(row.student)
    print(row.score)

    # So this is the best way to iterate row in pandas data frame




