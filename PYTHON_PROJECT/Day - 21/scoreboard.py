from turtle import Turtle

class Score(Turtle):
    def __int__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.points = 0
        self.update_score
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.points}", False, align= 'center', font=('Courier', 20, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align= 'center', font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.points += 1
