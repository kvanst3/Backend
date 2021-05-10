from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_pos()
        self.left(90)

    def move_forward(self):
        self.forward(5)

    def reset_pos(self):
        self.goto(0, -280)
