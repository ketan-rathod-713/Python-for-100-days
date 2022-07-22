# Working with file system and directories
# put highscore in turtle game

# Here i am unable to store the high score
# using python to read and write to file

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

file = open("my_file.txt")
contents = file.read()
print(contents)

file.close()  # so as it doesn't take bind all resources , just like lots of tabs are open

# as sometimes we may forgest so most python developer prefer

with open("my_file.txt") as file:
    contents2 = file.read()
    print(contents2)

# To write in file

with open("my_file.txt", mode="w") as file:  # By default mode is read to when write specify mode
    file.write("\n New text")

# if want to append then mode = "a"

# If you want to write a file and if doesn't exit then it will create this file from scratch for you

with open("new_file.txt", mode="w") as file:
    file.write("new text")

# file just dont have names , they have paths or directories
# There is one root and then all folder inside folder structure
# absolute file paths always starts with C or root
# Relative file paths are relative to working directory
# if we switch our working path then relative file pat will change
# if you want to go upward then ../
# ./file , if in same folder and we can remove ./

# we can also specify absolute file path
# in windows \ and in mac / separates folders

# if i want to show it relative to main.py 's relative folder

# for writting code main goal is to efficient code and write so that others understand

