from random import random
from tempfile import SpooledTemporaryFile

import random
art = ''' ____   __ __  ___ ___  ____     ___  ____        ____  __ __    ___  _____ _____
|    \ |  |  ||   |   ||    \   /  _]|    \      /    ||  |  |  /  _]/ ___// ___/
|  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )    |   __||  |  | /  [_(   \_(   \_ 
|  |  ||  |  ||  \_/  ||     ||    _]|    /     |  |  ||  |  ||    _]\__  |\__  |
|  |  ||  :  ||   |   ||  O  ||   [_ |    \     |  |_ ||  :  ||   [_ /  \ |/  \ |
|  |  ||     ||   |   ||     ||     ||  .  \    |     ||     ||     |\    |\    |
|__|__| \__,_||___|___||_____||_____||__|\_|    |___,_| \__,_||_____| \___| \___|
                                                                                 '''
print(art)
print("welcome to Number guessing game ")

def guess(start,end,number,steps):
    if(steps==0):
        print("You Loose this game ! Out of steps :|")
    else:
        print(f"{steps} steps left ")
        steps -= 1
        print(f"I am thinking the number between {start} and {end} ")
        guessNum = int(input("Enter your guess : "))
        if(guessNum==number): 
            print("You won this game wow :))) !!")
        elif guessNum > number:
            guess(start,guessNum,number,steps)
        else:
            guess(guessNum,end,number,steps)
        
        
difficulty = input("choose the difficulty (easy or hard) ? ")
RandNo = random.randint(0,100)
print(RandNo)
if(difficulty.lower()=="easy"):
    guess(0,100,RandNo,10)
else:
    guess(0,100,RandNo,5)
    
    
    
    
    # From angela 
    
    # from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()


