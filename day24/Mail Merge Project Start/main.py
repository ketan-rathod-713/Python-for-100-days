#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# first of all try with one name

# read demo

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    named_content = content.replace("[name]","ayush")

# now i got content , iterate all names
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

# Now iterate names

for i in names:
    print(i.find("\n"))
    i = i[:i.find("\n")]
    filepath = f"./Output/ReadyToSend/{i}.txt"
    with open(filepath,mode="w") as file:
        file.write(content.replace("[name]",i))

# The bug in this is that for last name it removes the last character instead of \n