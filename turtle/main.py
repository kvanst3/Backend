from turtle import Turtle, Screen
from math import floor
import random


def dash_line(turtle, dash_frequency, total_length):
    dash_amount = floor(total_length / dash_frequency)
    remainder = total_length % dash_frequency
    for _ in range(int(dash_amount/2)):
        turtle.pendown()
        turtle.forward(dash_frequency)
        turtle.penup()
        turtle.forward(dash_frequency)
    if remainder > 0:
        turtle.pendown()
        turtle.forward(remainder)


def generate_rgb():
    colors = range(1, 100)
    color = random.choice(colors)
    return color / 100


timmy = Turtle()
timmy.shape("turtle")
timmy.color("BlueViolet")
timmy.pencolor(0.1, 0.70, 0.12)

###Timmy makes a dashed square. And he is good at it.###

# timmy.penup()
# for _ in range(2):
#     timmy.forward(100)
#     timmy.left(90)

# timmy.pendown()
# for _ in range(4):
#     dash_line(timmy, 10, 200)
#     timmy.left(90)

angles = 3
for _ in range(8):
    timmy.pencolor(generate_rgb(), generate_rgb(), generate_rgb())
    degree = 360/angles
    timmy.seth(180 - degree)
    for _ in range(angles):
        timmy.forward(100)
        timmy.right(degree)
    angles += 1



screen = Screen()
screen.exitonclick()