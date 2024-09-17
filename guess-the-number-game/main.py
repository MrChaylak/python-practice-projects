#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def guess_checker(guess, ran_number, lives):
  keep_playing = True
  if guess == ran_number:
    print(f"You got it! The answer was: {ran_number}")
    keep_playing = False
  elif guess > ran_number:
    print("Too high.")
    lives -= 1
  else:
    print("Too low.")
    lives -= 1
  return lives, keep_playing

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

ran_number = random.randint(1, 100)
print(f"Answer: {ran_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
lives = 0
if difficulty == "hard" or difficulty == "h":
  lives = 5
else:
  lives = 10

keep_playing = True
while keep_playing:
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  lives, keep_playing = guess_checker(guess, ran_number, lives)
  if lives == 0:
    print(f"You have run out of guesses, you lose.\nThe answer was: {ran_number}")
    keep_playing = False
  elif keep_playing == True:
    print("Guess again.")
print("Thanks for playing!")