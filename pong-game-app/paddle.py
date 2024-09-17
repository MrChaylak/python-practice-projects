from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.coordinate = coordinate
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(UP)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(self.coordinate)

    def paddle_up(self):
        if self.ycor() < 250:
            self.setheading(UP)
            self.forward(20)
        else:
            self.goto(self.xcor(), 250)

    def paddle_down(self):
        if self.ycor() > -250:
            self.setheading(DOWN)
            self.forward(20)
        else:
            self.goto(self.xcor(), -250)
