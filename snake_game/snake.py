from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.sectors = []
        self.create_snake()
        self.head = self.sectors[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_sector(position)

    def add_sector(self, position):
        new_sector = Turtle("square")
        # new_sector.color("white")
        new_sector.color("DodgerBlue2")
        new_sector.penup()
        new_sector.goto(position)
        self.sectors.append(new_sector)

    def extend(self):
        self.add_sector(self.sectors[-1].position())

    def move(self):
        for sector_num in range(len(self.sectors) - 1, 0, -1):
            new_x = self.sectors[sector_num - 1].xcor()
            new_y = self.sectors[sector_num - 1].ycor()
            self.sectors[sector_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
