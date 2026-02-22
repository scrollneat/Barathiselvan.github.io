from turtle import *
import random

def draw_shape(sides):
  angle = 360/sides
  for sides in range (sides):
    vis.forward(50)
    vis.right(angle)

vis = Turtle()
vis.shape("classic")

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
colours = ['light gray', 'royal blue', 'gold','red','pink','cyan','aquamarine','burlywood', 'dark cyan', 'spring green', 'orange red', 'violet', 'dark olive green']
for i in range (3,20):
  vis.pencolor(random.choice(colours))
  draw_shape(i)
