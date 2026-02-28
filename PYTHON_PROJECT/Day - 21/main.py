#--------------------Snake game------------------------------------
from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
#screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = True
while game_over:
	time.sleep(0.1)
	screen.update()
	snake.move()
    
screen.exitonclick()
