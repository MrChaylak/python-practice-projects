import random
import hangman_words
import hangman_art
import os


def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS/Linux
    else:
        os.system('clear')


print(hangman_art.logo)
guessed_word = False
# word_list = ["aardvark", "baboon", "camel"]
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
guessed_words = []
lives = 12
print(f"You have {lives} lives.")

# Create blanks
display = []
for letter in chosen_word:
    display += "_"
print(f"{' '.join(display)}\n")

while not guessed_word:
    
    if "_" in display:
        guess = input("Guess a letter: ").lower()
        clear_console()
        
        if guess in guessed_words:
            print(f"You already guessed the word: {guess}")
            print(f"{' '.join(display)}")
            print(hangman_art.stages[lives])

        else:
            guessed_words += guess
            # print(guessed_words)
            
            # Check guessed letter
            correct = 0
            i = 0
            for letter in chosen_word:
                if letter == guess:
                    display[i] = letter
                    correct = 1
                i += 1
                
            if correct == 0:
                lives -= 1
                print(f"The letter \"{guess}\" is not in the word. You lose a life.")
                print(f"Lives left: {lives}")
                
            print(f"{' '.join(display)}")
            
            print(hangman_art.stages[lives])
            if lives == 0:
                print("You ran out of lives, game lost!")
                print(f'The solution was {chosen_word}.')
                break
    else:
        guessed_word = True
        print("You guessed the word!")

print("Thanks for playing!")