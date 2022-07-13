#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word = random.choice(word_list)
chances = 4
ans = []
for i in range(1,len(word)+1):
    ans+="_"
print(ans)   
 
while chances>0:
    a = input("Guess the letter ")
    flag = 0
    j = 0
    for i in word:
        if(a==i):
            ans[j] = a
            print("right")
            flag =1
        else:
            print("wrong")
        j += 1
    if flag==0:
        chances -=1
    print(ans)
    string = ''.join(ans)
    if(string==word):
        print("you have won")
        break
    if chances==0:
        print("lost !")    
    
    # .lower method in string
    # ''.join() method for list to string
    