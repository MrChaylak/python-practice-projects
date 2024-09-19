import os
from tkinter import *
import pandas
import random

current_card = {}

# Reading Data
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/english_words.csv")
finally:
    words_dict_list = data.to_dict(orient="records")
print(words_dict_list)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(words_dict_list)
    except IndexError:
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(card_title, text="Well Done!", fill="black", font=("Arial", 80, "bold"))
        canvas.itemconfig(card_word, text="You've memorized every card in this set.", fill="black",
                          font=("Arial", 30, "normal"))
        os.remove("./data/words_to_learn.csv")
    else:
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(card_title, fill="black", text="English")
        canvas.itemconfig(card_word, fill="black", text=current_card["English"])
        flip_timer = window.after(3000, card_flip)


# Flipping Card
def card_flip():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, fill="white", text="Turkish")
    canvas.itemconfig(card_word, fill="white", text=current_card["Turkish"])


# Removing Words User Knows
def remove_card():
    words_dict_list.remove(current_card)
    next_card()


# UI
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards Learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Message box?

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Text", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, borderwidth=0, highlightthickness=0, command=remove_card)
right_btn.grid(column=1, row=1)

flip_timer = window.after(3000, card_flip)
next_card()

window.mainloop()

df = pandas.DataFrame(words_dict_list)
df.to_csv("./data/words_to_learn.csv", index=False)
