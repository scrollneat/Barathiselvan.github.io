from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 20, "normal"))
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 20, "normal"))
        
    
    def score_r_increase(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
    
    def score_l_increase(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()