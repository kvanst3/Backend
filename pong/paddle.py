from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=3, outline=0)
        self.left(90)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        self.forward(15)

    def move_down(self):
        self.backward(15)
