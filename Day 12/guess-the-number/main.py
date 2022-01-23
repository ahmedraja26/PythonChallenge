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

print(logo)
print("Welcome to the Number Guessing Game!")

diffculty = input("Choose a difficulty. Type 'easy' or 'hard':")
if (diffculty == "easy"):
  numOfGuesses = 10
else:
  numOfGuesses = 5
print(f"You have {numOfGuesses} attempts remaining to guess the number")

number = random.randint(1,100)
won = False

while numOfGuesses > 0 and won == False:
  guess = int(input("Make a guess: "))
  numOfGuesses -= 1

  if(guess == number):
    print("Correct")
    won = True
  elif guess > number:
    print("Too High")
    print(f"You have {numOfGuesses} attempts remaining to guess the number")
  else:
    print("Too low")
    print(f"You have {numOfGuesses} attempts remaining to guess the number")

if numOfGuesses == 0 and won == False:
  print("You lose")




