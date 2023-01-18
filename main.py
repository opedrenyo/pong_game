from turtle import Turtle, Screen
from player import Player
from ball import Ball
from score import Score
from midfield import Midfield
import time


NOT_SCORE = True
BALL_DISTANCE = 14

screen = Screen()
screen.setup(width=1200, height = 800)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

player_1 = Player("player_1")
player_2 = Player("player_2")
midfield = Midfield()
ball = Ball()
score_player_1 = Score("Score_1")
score_player_2 = Score("Score_2")


screen.listen()
screen.onkeypress(key= "Up", fun=player_1.move_up)
screen.onkeypress(key= "Down", fun=player_1.move_down)
screen.onkeypress(key="w", fun=player_2.move_up)
screen.onkeypress(key="s", fun=player_2.move_down)
screen.onkeypress(key="Return", fun=ball.move)


while NOT_SCORE:
    screen.update()
    time.sleep(0.001)
    ball.move()
    if ball.ycor() >= 385 or ball.ycor() <= -385:
        ball.wall_colission()
    if ball.xcor() >= 595:
        ball.goal()
        ball.speed = 5
        score_player_1.increase()
        player_1.players_after_goal()
        player_2.players_after_goal()
        screen.update()
        time.sleep(2)
    elif ball.xcor() <= -595:
        ball.goal()
        ball.speed = 5
        score_player_2.increase()
        player_1.players_after_goal()
        player_2.players_after_goal()
        screen.update()
        time.sleep(2)

    elif ball.distance(player_1.top_b) < BALL_DISTANCE:
        ball.topside_player_collission()
        ball.increase_speed()
    elif ball.distance(player_1.bot_b) < BALL_DISTANCE:
        ball.botside_player_collission()
        ball.increase_speed()
    elif ball.distance(player_1.second_b) < BALL_DISTANCE or ball.distance(player_1.third_b) < BALL_DISTANCE or ball.distance(player_1.fourth_b) < BALL_DISTANCE:
        ball.mid_player_colission()
        ball.increase_speed()
    elif ball.distance(player_2.top_b) < BALL_DISTANCE:
        ball.topside_player_collission()
        ball.increase_speed()
    elif ball.distance(player_2.bot_b) < BALL_DISTANCE:
        ball.botside_player_collission()
        ball.increase_speed()
    elif ball.distance(player_2.second_b) < BALL_DISTANCE or ball.distance(player_2.third_b) < BALL_DISTANCE or ball.distance(player_2.fourth_b) < BALL_DISTANCE:
        ball.mid_player_colission()
        ball.increase_speed()

screen.exitonclick()