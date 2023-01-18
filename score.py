from turtle import Turtle

class Score(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.up()
        self.hideturtle()
        self.color("white")
        self.score = 0
        if self.name == "Score_1":
            self.set_score_1()
        elif self.name == "Score_2":
            self.set_score_2()
        self.write(arg=self.score, align="center", font=("calibri",50,"bold"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(arg=self.score, align="center", font=("calibri",50,"bold"))
        
    def set_score_1(self):
        self.goto(x = -130, y = 300)
        
    def set_score_2(self):
        self.goto(x = 130, y = 300)