import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)
player = Player()
car = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()

    # Detect when the turtle player collides with a car
    for i in car.allcars:
        if player.distance(i) < 20:
            game_on = False
            level.game_over()
    
    # Detect when the turtle player reached the top edge of the screen
    if player.at_finish():
        player.home_place()
        car.fast_up()
        level.level_up()

screen.exitonclick()