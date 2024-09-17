from turtle import Turtle, Screen
import random

is_race_on = False
background = 'racetrack.png'
screen = Screen()
screen.bgpic(background)
screen.setup(width=500, height=744)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-325, -200, -75, 58, 190, 325]
turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2)
    new_turtle.color(colors[3])
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost! The {winner_color} turtle is the winner!")
        random_step = random.randint(1, 10)
        turtle.forward(random_step)

screen.exitonclick()
