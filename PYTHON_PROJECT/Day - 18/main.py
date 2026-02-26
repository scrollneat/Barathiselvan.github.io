import turtle
import random

# ----------------------Common Functions--------------------------------------------------------------------------
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

# ----------------------Declarations--------------------------------------------------------------------------
vis = turtle.Turtle()
vis.hideturtle()
vis.speed(0)

##-------------------Challenge 1 Draw a square--------------------------------------------------------------
def draw_square():
  vis.home()
  for i in range (4):
    vis.forward(100)
    vis.left(90)
  vis.clear()
draw_square()
##-------------------Challenge 2 Drawing Dashed line--------------------------------------------------
def draw_dashed_line():
  vis.home()
  for i in range (15):
    vis.pendown()
    vis.forward(10)
    vis.penup()
    vis.forward(10)
  vis.clear()
  
draw_dashed_line()
##-------------------Challenge 3 Drawing different shapes--------------------------------------------------
def draw_diff_shapes():
  # vis.setposition(-50,200)
  vis.home()
  vis.pendown()
  # colours = ['light gray', 'royal blue', 'gold','red','pink','cyan','aquamarine','burlywood', 'dark cyan', 'spring green', 'orange red', 'violet', 'dark olive green']
  for i in range (3,12):
    vis.pencolor(random_color())
    draw_shape(i)
  vis.clear()
draw_diff_shapes()

##-------------------Challenge 4 Generate Random walk----------------------------------------
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


##-------------------Challenge 5 Spirograph----------------------------------------
def draw_spirograph(size_of_gap):
    vis.penup()
    vis.home()
    vis.pendown()
    vis.pensize(1)
    for _ in range(int(360 / size_of_gap)):
        vis.color(random_color())
        vis.circle(100)
        vis.setheading(vis.heading() + size_of_gap)

draw_spirograph(5)
