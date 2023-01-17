from turtle import Turtle, Screen
from player import Player_1, Player_2
from ball import Ball
import time

GAME_IS_ON = True


screen = Screen()
screen.setup(width=1200, height = 800)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

player_1 = Player_1()
player_2 = Player_2()
ball = Ball()


screen.listen()
screen.onkeypress(key= "Up", fun=player_1.move_up)
screen.onkeypress(key= "Down", fun=player_1.move_down)
screen.onkeypress(key="w", fun=player_2.move_up)
screen.onkeypress(key="s", fun=player_2.move_down)







while GAME_IS_ON:
    screen.update()
    time.sleep(0.01)
    ball.move()






screen.exitonclick()