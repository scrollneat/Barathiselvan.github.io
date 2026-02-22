import turtle
import random


def draw_shape(sides):
  angle = 360/sides
  for sides in range (sides):
    vis.forward(50)
    vis.right(angle)

# turtle.colormode(255)
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  ran_color = (r,g,b)
  return ran_color
vis = turtle.Turtle()
vis.shape("classic")
vis.speed(0)

for i in range (4):
  vis.forward(100)
  vis.left(90)

vis.clear()

for i in range (10):
  vis.pendown()
  vis.forward(10)
  vis.penup()
  vis.forward(10)
  
vis.clear()

vis.setposition(-50,200)
vis.clear()

vis.pendown()
# colours = ['light gray', 'royal blue', 'gold','red','pink','cyan','aquamarine','burlywood', 'dark cyan', 'spring green', 'orange red', 'violet', 'dark olive green']
for i in range (3,12):
  vis.pencolor(random_color())
  draw_shape(i)
vis.clear()

vis.pendown()
vis.pensize(10)
direction = [0, 90, 180, 270, 360]
vis.setposition(25,0)
vis.clear()
for i in range (100):
  vis.forward(20)
  vis.pencolor(random_color())
  vis.left(random.choice(direction))
vis.clear()

for i in range (20):
  vis.pendown()
  vis.circle(5)
  vis.pencolor(random_color())
  vis.penup()
  vis.forward(20)
  turtle.tilt(45)
  vis.pendown()
