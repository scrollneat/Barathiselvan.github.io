from turtle import Turtle
import random
COLORS = ["red", "orange", "blue", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20

class CarManager():
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE
      
    def generate_car(self):
        random_num = random.randint(1,6)
        if random_num == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            new_car.setheading(180)
            self.allcars.append(new_car)
    
    def move_car(self):
        for i in self.allcars:
            i.forward(self.car_speed)

    def fast_up(self):
        self.car_speed  += MOVE_INCREMENT
