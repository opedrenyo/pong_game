from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.score = 0

        def increase(self):
            self.score += 1
        
class Score_1(Score):
    def __init__(self):
        super().__init__()
        self.goto(x = -150, y = 300)
        self.write(arg=self.score, align="center", font=("calibri",50,"bold"))

class Score_2(Score):
    def __init__(self):
        super().__init__()
        self.goto(x = 150, y = 300)
        self.write(arg=self.score, align="center", font=("calibri",50,"bold"))



