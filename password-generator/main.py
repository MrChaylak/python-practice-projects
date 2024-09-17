#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for letter in range(0, nr_letters):
  password += random.choice(letters)
for symbol in range(0, nr_symbols):
  password += random.choice(symbols)
for number in range(0, nr_numbers):
  password += random.choice(numbers)
# print(password)

list_password = list(password)
# print(list_password)

input_len = nr_letters + nr_symbols + nr_numbers
rand_password = ""
for char in range(0, input_len):
  already_picked = random.choice(list_password)
  rand_password += already_picked
  list_password.remove(already_picked)
print(rand_password)
# print(list_password)
