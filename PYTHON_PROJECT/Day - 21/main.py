#--------------------Snake game------------------------------------
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
#screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  

  #Detect snake collision with the food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score.increase_score()

  #Detech Collision with the wall
  if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or (snake.head.ycor() > 290) or (snake.head.ycor() < -290):
    game_on = False
    score.game_over()

  #Detech Collision with the snake tail
  for i in snake.new_snake_list:
    if i == snake.head:
      pass
    elif snake.head.distance(i) < 10:
      game_on = False
      score.game_over()

  

screen.exitonclick()
