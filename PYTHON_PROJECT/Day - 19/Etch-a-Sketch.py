#--------------------Etch-a-Sketch App------------------------------------

from turtle import Turtle, Screen

vis = Turtle()
screen = Screen()

def move_forward():
	vis.forward(10)
  
def move_backwards():
	vis.backward(10)

def move_left():
	new_heading = vis.heading() + 10
	vis.left(vis.setheading(new_heading))
  
def move_right():
	new_heading = vis.heading() - 10
	vis.setheading(new_heading)

def clean():
  vis.clear()
  vis.penup()
  vis.home()
  vis.pendown()
  
screen.listen()
screen.onkey(move_forward , 'w')
screen.onkey(move_backwards , 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clean, 'c')
screen.exitonclick()
