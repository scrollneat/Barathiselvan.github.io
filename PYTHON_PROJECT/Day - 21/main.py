#--------------------Snake game------------------------------------

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
#screen.title("Snake Game")
screen.tracer(0)
positions = []
for i in range(0,41,20):
	turtle_1 = Turtle()
	turtle_1.penup()
	turtle_1.color('white')
	turtle_1.shape('square')
	turtle_1.goto(-i, 0)
	positions.append(turtle_1)

game_over = True
while game_over:
	time.sleep(0.1)
	screen.update()
	for part in positions:
		part.forward(20)
		
screen.exitonclick()
