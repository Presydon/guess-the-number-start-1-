#Number Guessing Game Objectives:

# Include an ASCII art logo.

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear



def easy():
    attempts = 10
    if attempts != 0:
        while attempts >= 1:
            guess_number = int(input("Make a guess: "))
            if guess_number > NUMBER_THINK:
                print("Too high.. 🤣")
                attempts -= 1
                print("Guess Again")
                print(f"You have {attempts} left \n" )
            elif guess_number < NUMBER_THINK:
                print("Too low.. 😂")
                attempts -= 1
                print("Guess Again")
                print(f"You have {attempts} left \n")
            elif guess_number == NUMBER_THINK:
                print("You Guessed correctly 👍 \n")
                break
            
def hard():
    attempts = 5
    if attempts > 0:
        while attempts > 0:
            guess_number = int(input("Make a guess: "))
            if guess_number > NUMBER_THINK:
                print("Too high.. 🤣")
                attempts -= 1
                print("Guess Again")
                print(f"You have {attempts} left \n")             
            elif guess_number < NUMBER_THINK:
                print("Too low.. 😂")
                attempts -= 1
                print("Guess Again")
                print(f"You have {attempts} left \n")
            elif guess_number == NUMBER_THINK:
                print("You Guessed correctly 👍 \n")
                break
      
NUMBER_THINK = random.choice(range(1,101))
def play_game():
    print(logo)
    print("Welcome to Number Guessing Game 🥰 ")
    print("I'm thinking of a Number between 1 and 100 ")
    print(f"Number is {NUMBER_THINK} ")
    difficulty = input('Choose difficulty "Easy" or "Hard" ')
    if difficulty == "easy".lower():
      easy()
    elif difficulty == "hard".lower():
      hard()
    else:
        print("Invalid Option")
    
play_game()
while input("Would you like to Guess again? 'Yes' or 'No' ") == "yes".lower():
  clear()
  play_game()
else:
  print("Byee...")
