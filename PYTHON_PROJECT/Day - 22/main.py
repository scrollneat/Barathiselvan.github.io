import turtle
from paddle import PaddleStick
#----------initialize screen-----------------------------------------
pong_border = turtle.Turtle()
screen = turtle.Screen()
width = 800
height = 600
screen.bgcolor("black")
screen.setup(width=width, height=height)
screen.title("Pong Game")
screen.tracer(0)
#-----------------------------------------------------------------------

#------------Drawing Border line ----------------------------------------------
pong_border.color("white")
pong_border.penup()
pong_border.goto(-width/2 + 10, height/2 - 10)
pong_border.pendown()

#  Draw Rectangle
for _ in range(2):
    pong_border.forward(width - 20) # Width of border
    pong_border.right(90)
    pong_border.forward(height - 20) # Height of border
    pong_border.right(90)
#-------------------------------------------------------------------------
right_paddle = PaddleStick((360,0))
left_paddle = PaddleStick((-360,0))

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


game_on = True
while game_on:
    screen.update()

screen.exitonclick()