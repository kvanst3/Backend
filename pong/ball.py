from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        time.sleep(1)
        self.goto(0, 0)
        self.move_speed = 0.04
        self.bounce_paddle()
