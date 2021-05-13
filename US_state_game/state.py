from turtle import Turtle


class State(Turtle):

    def __init__(self, state_name, x, y):
        super().__init__()
        self.ht()
        self.speed(3)
        self.penup()
        self.goto(int(x), int(y))
        self.write(f"{state_name}")
