import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

car_manager.generate_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    if player.is_at_finish():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.increase_speed()
        print("hello")

    for car in car_manager.cars:
        car_y = car.ycor()
        player_y = player.ycor()
        abs_y = abs(car_y - player_y)
        # No need to measure the player as we know it is always at X = 0
        abs_x = abs(car.xcor())
        if abs_y < 18 and abs_x <= 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
