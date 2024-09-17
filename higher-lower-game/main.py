import random
from game_data import data
from art import logo, vs
import os


def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS/Linux
    else:
        os.system('clear')


print(logo)

score = 0
answer = ""
choice = ""

compare_a = random.choice(data)
data.remove(compare_a)
play_game = True
while play_game:
  print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}" )
  print(vs)
  compare_b = random.choice(data)
  data.remove(compare_b)
  print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}" )
  
  if compare_a["follower_count"] > compare_b["follower_count"]:
    answer = "A"
  else:
    answer = "B"
  
  correct_input = False
  while not correct_input:
    choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    if choice == "A" or choice == "B":
      correct_input = True
    else:
      print("Wrong input, try again.")
      
  clear_console()
  print(logo)
  if choice == answer:
    compare_a = compare_b
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    play_game = False

print("Thanks for playing!")