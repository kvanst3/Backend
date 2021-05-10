from turtle import Turtle
import random
import time
COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown']


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=0.8, stretch_len=2, outline=0)
        random_y = random.randint(-260, 260)
        self.goto((-320, random_y))
        # self.speed = 0.07

    def move_forward(self):
        self.forward(10)
        # time.sleep(self.speed)
