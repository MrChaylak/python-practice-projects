import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


hands = [rock, paper, scissors]
keep_playing = "yes"

while keep_playing == "yes":       
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    player_choice = int(input())
    if player_choice >= 3 or player_choice < 0:
        print("You typed an invalid number, you lose!")
    else:
        player_hand = hands[player_choice]
        computer_hand = hands[random.randint(0,2)]
        print(player_hand)
        print("Computer chose:")
        print(computer_hand)
        if player_hand == rock:
            if computer_hand == rock:
                print("Draw")
            elif computer_hand == paper:
                print("You lose")
            else:
                print("You win")
        elif player_hand == paper:
            if computer_hand == rock:
                print("You win")
            elif computer_hand == paper:
                print("Draw")
            else:
                print("You lose")
        else:
            if computer_hand == rock:
                print("You lose")
            elif computer_hand == paper:
                print("You win")
            else:
                print("Draw")
        print("Do you want to play again? Type 'yes' or 'no'.")
        keep_playing = input().lower()
        if keep_playing != "yes" and keep_playing != "no":
            print("You typed an invalid answer, you lose!")
        else:
            if keep_playing == "no":
                print("Thanks for playing!")
            