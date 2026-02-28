import turtle
class Snake:
    def __int__(self):
        self.segment = Turtle()
        self.positions = []
        for i in range(0, 41, 20):
            self.segment.penup()
            self.segment.color('white')
            self.segment.shape('square')
            self.segment.goto(-i,0)
            self.positions.append(segment)

    def move(self):
        for pos_num in range(len(self.positions) -1, 0, -1):
            new_x = self.positions[pos_num - 1].xcor()
            new_y = self.positions[pos_num - 1].ycor()
            self.positions[pos_num].goto(new_x,new_y)
            self.positions[0].forward(20)
            

