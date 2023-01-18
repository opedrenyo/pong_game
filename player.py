from turtle import Turtle

PLAYER_INITIAL_POSITION = [(0, 50), (0, 30), (0, 10), (0, -10), (0, -30)]
PLAYER_1_XCOR = -550
PLAYER_2_XCOR = 550
SPEED = 20


class Player(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.player = []
        self.create_new_player()
        self.player_ycor = 50
        self.top_b = self.player[0]
        self.second_b = self.player[1]
        self.third_b = self.player[2]
        self.fourth_b = self.player[3]
        self.bot_b = self.player[4]
        self.length = len(self.player)

        if self.name == "player_1":
            self.set_player_1()
        elif self.name == "player_2":
            self.set_player_2()

    def create_new_player(self):
        for position in PLAYER_INITIAL_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.up()
            new_segment.setheading(90)
            new_segment.goto(position)
            self.player.append(new_segment)

    def move_up(self):
        for seg in range(self.length-1, 0, -1):
            new_position = self.player[seg-1].position()
            self.player[seg].goto(new_position)
        self.top_b.forward(SPEED)
        
    def move_down(self):
        for seg in range(0, self.length-1):
            new_position = self.player[seg+1].position()
            self.player[seg].goto(new_position)
        self.bot_b.setheading(270)
        self.bot_b.forward(SPEED)

    def set_player_1(self):
        for seg in self.player:
            seg.setx(PLAYER_1_XCOR)
            

    def set_player_2(self):
        for seg in self.player:
            seg.setx(PLAYER_2_XCOR)

    def players_after_goal(self):
        for seg in self.player:
            seg.sety(self.player_ycor)
            self.player_ycor -= 20

        
            


    