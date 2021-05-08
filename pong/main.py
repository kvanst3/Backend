from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle((-365,0))
player2 = Paddle((365, 0))
ball = Ball()

screen.listen()
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")
screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(.06)


screen.exitonclick()
