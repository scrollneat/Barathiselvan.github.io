import turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.positions = []
        self.snake_body()
        self.head = self.positions[0]

    def snake_body(self):
        for i in range(0, 41, 20):
            self.segment = turtle.Turtle()
            self.segment.penup()
            self.segment.color('white')
            self.segment.shape('square')
            self.segment.goto(-i,0)
            self.positions.append(self.segment)

    def move(self):
        for pos_num in range(len(self.positions) -1, 0, -1):
            new_x = self.positions[pos_num - 1].xcor()
            new_y = self.positions[pos_num - 1].ycor()
            self.positions[pos_num].goto(new_x,new_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)