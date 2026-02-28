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
	
	for pos_num in range(len(positions) -1, 0, -1):
		new_x = positions[pos_num - 1].xcor()
		new_y = positions[pos_num - 1].ycor()
		positions[pos_num].goto(new_x,new_y)
	positions[0].forward(20)
    
screen.exitonclick()
