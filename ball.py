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
    
    def move(self):
        self.forward(3)

