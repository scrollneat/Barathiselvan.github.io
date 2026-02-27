#--------------------Snake game------------------------------------

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
#screen.title("Snake Game")
positions = []

for i in range(0,41,20):
	turtle_1 = Turtle()
	turtle_1.color('white')
	turtle_1.shape('square')
	turtle_1.goto(-i, 0)
  

screen.exitonclick()
