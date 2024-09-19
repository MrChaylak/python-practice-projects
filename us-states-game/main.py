import turtle
import pandas
from tkinter import messagebox

ALIGNMENT = "center"
STATE_FONT = ('Arial', 10, 'normal')
SCORE_FONT = ('Arial', 20, 'normal')
STATE_COUNT = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

s = turtle.Turtle()
s.penup()
s.hideturtle()
s.goto(0, 270)


states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()
# 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 to test game end
already_answered = []

with open("data.txt") as file:
    high_score = int(file.read())

correct_guess = 0
s.write(f"Score: {correct_guess} High Score: {high_score}", align=ALIGNMENT, font=SCORE_FONT)
answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()
while len(already_answered) < STATE_COUNT:
    if answer_state == "Exit":
        break
    elif answer_state in already_answered:
        answer_state = screen.textinput(title=f"{correct_guess}/{STATE_COUNT} States Correct",
                                        prompt="Already answered!\nWhat's another state's name?").title()
    elif answer_state in states_list:
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_info = states_data[states_data.state == answer_state]
        state.goto(state_info.x.item(), state_info.y.item())
        state.write(answer_state, align=ALIGNMENT, font=STATE_FONT)
        correct_guess += 1
        if correct_guess > high_score:
            high_score = correct_guess
            with open("data.txt", mode="w") as file:
                file.write(str(high_score))
        s.clear()
        s.write(f"Score: {correct_guess} High Score: {high_score}", align=ALIGNMENT, font=SCORE_FONT)
        already_answered.append(answer_state)
        if len(already_answered) < STATE_COUNT:
            answer_state = screen.textinput(title=f"{correct_guess}/{STATE_COUNT} States Correct",
                                            prompt="What's another state's name?").title()
        else:
            messagebox.showinfo("Congratulations", "You guessed every state!")
    else:
        answer_state = screen.textinput(title=f"{correct_guess}/{STATE_COUNT} States Correct",
                                        prompt="Wrong answer, try again.\nWhat's another state's name?").title()

not_guessed_states = [state for state in states_list if state not in already_answered]
print(not_guessed_states)
df = pandas.DataFrame(not_guessed_states)
df.to_csv("states_to_learn.csv")

states_to_learn = pandas.read_csv("states_to_learn.csv")
print(states_to_learn)

print("Game Exit")

# screen.exitonclick()
