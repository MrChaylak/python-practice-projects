import random
# from replit import clear
from art import logo
import os


def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS/Linux
    else:
        os.system('clear')


# Define the initial deck
def create_deck():
  return [
      2,
      2,
      2,
      2,
      3,
      3,
      3,
      3,
      4,
      4,
      4,
      4,
      5,
      5,
      5,
      5,
      6,
      6,
      6,
      6,
      7,
      7,
      7,
      7,
      8,
      8,
      8,
      8,
      9,
      9,
      9,
      9,
      10,
      10,
      10,
      10,
      10,  # Jacks
      10,
      10,
      10,
      10,  # Queens
      10,
      10,
      10,
      10,  # Kings
      10,
      10,
      10,
      11,  # Aces
      11,
      11,
      11
  ]


# Initialize the deck and shuffle
cards = create_deck()
random.shuffle(cards)

money = 1000


def money_bet_checker(money):
  money, bet = bet_money(money)
  return money, bet


def bet_money(money):
  chips = [10, 50, 100, 200, 500, 1000]
  print(f"Your money is: {money}")
  print("Available chips:", chips)
  total_bet = 0

  while True:
    try:
      bet_pick = input(
          "Enter the value of a chip you want to bet, type 'a' for 'All In', or 'q' to quit betting: "
      ).strip().lower()

      if bet_pick == 'a':
        # Bet all remaining money
        total_bet = money
        money = 0
        print(f"Total bet is all in: {total_bet}")
        break

      elif bet_pick == 'q':
        if total_bet == 0:
          print("You have to bet to play")
        else:
          # Quit betting and proceed with current bet
          print(f"Total bet is: {total_bet}")
          break

      else:
        bet_pick = int(
            bet_pick)  # Convert input to integer to check chip value
        if bet_pick in chips:
          chip_count = int(
              input(f"How many {bet_pick} chips do you want to bet? "))
          current_bet = bet_pick * chip_count

          if current_bet > money:
            print(
                f"You don't have enough money. Your current money: {money} and current bet: {total_bet}"
            )
          else:
            total_bet += current_bet
            money -= current_bet
            print(f"Current total bet: {total_bet}")

            # Check if money is depleted
            if money <= 0:
              print(
                  "You don't have enough money to place a bet anymore. Betting is stopped."
              )
              break
        else:
          print("Invalid chip value. Please choose from the list.")

    except ValueError:
      print("Invalid input. Please enter a valid number or option.")

  return money, total_bet


def deal_card():
  global cards
  # print(cards)
  # Check if the deck is empty
  if not cards:
    print("Deck is empty. Re-shuffling...")
    cards = create_deck()  # Regenerate the deck
    random.shuffle(cards)  # Shuffle the new deck
  # Deal a card
  picked_card = cards.pop()
  return picked_card


def score_tracker(cards_list, player_name):
  if 11 in cards_list and 10 in cards_list and player_name != "Dealer":
    print("You got Blackjack!")
  return sum(cards_list)


def ace_checker(cards, score):
  if 11 in cards and score > 21:
    for card in range(len(cards)):
      if cards[card] == 11:
        cards[card] = 1
        score -= 10
        break
  return cards, score


def winner_checker(player_score, cpu_score, money, bet):
  if player_score > 21:
    print(f"You went over. You lose 😭\nMoney: {money}")
    return money
  elif cpu_score > 21:
    if player_score == 21:
      money += bet * 2.5
      print(f"You got blackjack!!! Pay is 3:2\nMoney: {money}")
      return money
    else:
      money += bet * 2
      print(f"Opponent went over. You win 😁\nMoney: {money}")
      return money
  elif player_score == cpu_score:
    money += bet
    print(f"It is a draw 😅\nMoney: {money}")
    return money
  else:
    if player_score > cpu_score:
      if player_score == 21:
        money += bet * 2.5
        print(f"You got blackjack!!! Pay is 3:2\nMoney: {money}")
        return money
      else:
        money += bet * 2
        print(f"You win 😀\nMoney: {money}")
        return money
    else:
      print(f"You lose 😤\nMoney: {money}")
      return money

def blackjack():
  print(logo)
  player_cards = []
  cpu_cards = []
  player_score = 0
  cpu_score = 0
  cpu_pick = True
  player_name = "Player"
  cpu_name = "Dealer"
  global money
  money, bet = money_bet_checker(money)

  for card in range(2):
    player_cards.append(deal_card())
    cpu_cards.append(deal_card())
  # player_cards = [10, 11]
  # cpu_cards = [10, 11]
  # player_cards = [10, 10]
  # cpu_cards = [10, 10]
  player_score = score_tracker(player_cards, player_name)
  cpu_score = score_tracker(cpu_cards, cpu_name)
  player_cards, player_score = ace_checker(player_cards, player_score)
  cpu_cards, cpu_score = ace_checker(cpu_cards, cpu_score)

  print(f"Your cards: {player_cards}, current score: {player_score}")
  print(f"Computer's first card: {cpu_cards[0]}")
  # print(cpu_cards)

  while player_score < 21:
    card_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if card_choice == "n":
      break
    else:
      player_cards.append(deal_card())
      player_score = score_tracker(player_cards, player_name)
      player_cards, player_score = ace_checker(player_cards, player_score)
      print(f"Your cards: {player_cards}, current score: {player_score}")
      print(f"Computer's first card: {cpu_cards[0]}")

  if player_score > 21:
    cpu_pick = False
  while cpu_pick:
    while cpu_score < 17:
      cpu_cards.append(deal_card())
      cpu_score = score_tracker(cpu_cards, cpu_name)
      cpu_cards, cpu_score = ace_checker(cpu_cards, cpu_score)
    cpu_pick = False

  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")

  money = winner_checker(player_score, cpu_score, money, bet)


keep_playing = True
while keep_playing:
  if money == 0:
    print("You have no money left! Better luck next time.")
    keep_playing = False
    break
  play_choice = input(
      "Do you want to play a game of blackjack? Type 'y' or 'n': ")
  if play_choice == "n":
    keep_playing = False
  else:
    clear_console()
    blackjack()
print(f"Your final money is: {money}")
print("Thanks for playing!")
