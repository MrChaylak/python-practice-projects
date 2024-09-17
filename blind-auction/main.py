from art import logo
import os


def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS/Linux
    else:
        os.system('clear')


print(logo)

bidders_done = False
bidders = {}
best_bid = 0
winner = ""

while not bidders_done:
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What is your bid?: $"))
  bidders[bidder_name] = bid_amount

  check_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if check_bidders == "no":
    bidders_done = True
  else:
    clear_console()
for bidder in bidders:
  if bidders[bidder] > best_bid:
    best_bid = bidders[bidder]
    winner = bidder

print(f"The winner is {winner} with a bid of ${best_bid}")