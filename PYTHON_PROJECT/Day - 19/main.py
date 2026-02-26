#--------------------Etch-a-Sketch App------------------------------------

from turtle import Turtle, Screen

vis = Turtle()
screen = Screen()

def move_forward():
	vis.setheading(0)
	vis.forward(50)
  
def move_backwards():
	vis.setheading(180)
	vis.forward(50)

def move_counter_clockwise():
	vis.setheading(30)
	vis.circle(100, 40)
  
def move_clockwise():
	vis.setheading(180)
	vis.circle(50, 10)

def clean():
  vis.clear()
  vis.home()
  
screen.listen()
screen.onkey(move_forward , 'w')
screen.onkey(move_backwards , 's')
screen.onkey(move_counter_clockwise, 'a')
screen.onkey(move_clockwise, 'd')
screen.onkey(clean, 'c')


