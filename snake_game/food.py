from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("white")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randrange(-290, 290, 10)
        random_y = random.randrange(-290, 290, 10)
        self.goto(random_x, random_y)
