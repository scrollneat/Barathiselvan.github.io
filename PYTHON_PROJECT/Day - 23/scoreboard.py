from turtle import Turtle 
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align = "center", font = FONT)
    
    def level_up(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align = "center", font = FONT)


    