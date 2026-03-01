import turtle
from paddle import PaddleStick
from ball import Ball
import time
from scoreboard import Score
#----------initialize screen-------------------------------------------------------------------------------------------------------------------------------------------
pong_border = turtle.Turtle()
screen = turtle.Screen()
width = 800
height = 600
screen.bgcolor("black")
screen.setup(width=width, height=height)
screen.title("Pong Game")
screen.tracer(0)
#----------------------------------------------------------------------------------------------------------------------------------

# #------------Drawing Border line -------------------------------------------------------------------------------------------------------------------------
# pong_border.color("white")
# pong_border.penup()
# pong_border.goto(-width/2 + 10, height/2 - 10)
# pong_border.pendown()

# #  Draw Rectangle
# for _ in range(2):
#     pong_border.forward(width - 20) # Width of border
#     pong_border.right(90)
#     pong_border.forward(height - 20) # Height of border
#     pong_border.right(90)
#-------------------------------------------------------------------------
right_paddle = PaddleStick((360,0))
left_paddle = PaddleStick((-360,0))

ball = Ball()
score = Score()
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting ball collision at top and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()
    
    # detecting collision when ball hits the paddle
    if ball.distance(right_paddle) < 30 and ball.xcor() > 320  or ball.distance(left_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_x_axis()


    # detecting when paddle misses the ball
    if ball.xcor() > 380 :
        ball.reset()
        score.score_l_increase()
    
    if ball.xcor() < -380:
        ball.reset()
        score.score_r_increase()
screen.exitonclick()