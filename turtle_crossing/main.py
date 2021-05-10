from turtle import Screen
from player import Player
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

player = Player()
screen.listen()
scoreboard = Scoreboard()


game_on = True
while game_on:
    screen.onkey(player.move_forward, "w")
    screen.update()
    if player.ycor() >= 280:
        player.reset_pos()
        screen.onkey(None, "w")
        scoreboard.increase_level(screen)
        #increase car speed



screen.exitonclick()
