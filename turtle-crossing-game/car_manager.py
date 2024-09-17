from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_NUMBER = 30


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for _ in range(CAR_NUMBER):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(-290, 330), random.randint(-8, 9)*25)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
            if car.xcor() < -300:
                car.goto(330, random.randint(-8, 9)*25)
                car.color(random.choice(COLORS))

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
