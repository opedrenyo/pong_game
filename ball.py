from turtle import Turtle
import random

INITIAL_RANDOM_MOVEMENT = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.setheading(random.choice(INITIAL_RANDOM_MOVEMENT))
        self.speed = 5
    
    def move(self):
        self.forward(self.speed)

    def wall_colission(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 135:
            self.setheading(225)
        elif self.heading() == 315:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(135)

    def mid_player_colission(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(315)

    def topside_player_collission(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 315:
            self.setheading(135)
        elif self.heading() == 225:
            self.setheading(45)

    def botside_player_collission(self):
        if self.heading() == 45:
            self.setheading(225)
        elif self.heading() == 135:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(315)

    def goal(self):
        self.home()
        self.setheading(random.choice(INITIAL_RANDOM_MOVEMENT))

    def increase_speed(self):
        self.speed *= 1.05 
