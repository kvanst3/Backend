from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
player1 = Paddle((-365,0))
player2 = Paddle((365, 0))
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")
screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")

while scoreboard.player1 + scoreboard.player2 < 5:
    game_on = True
    while game_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 285 or ball.ycor() < -285:
            ball.bounce_wall()

        # Detect collision with paddle
        if ball.distance(player1) < 45 and  ball.xcor() == - 350 or ball.distance(player2) < 45 and ball.xcor() == 350:
            ball.bounce_paddle()

        # Detect if ball goes out of bound
        if ball.xcor() > 410:
            scoreboard.increase_score("p1")
            ball.reset_ball()
            game_on = False

        elif ball.xcor() < - 410:
            scoreboard.increase_score("p2")
            ball.reset_ball()
            game_on = False
        
        

scoreboard.game_over()
screen.exitonclick()
