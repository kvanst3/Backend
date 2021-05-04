from turtle import Turtle, Screen
from math import floor
import random
import colorgram


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
    r = random.randint(1, 100) / 100
    g = random.randint(1, 100) / 100
    b = random.randint(1, 100) / 100
    return (r, g, b)


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

###Timmy draws increasingly complex figures.###
 
# angles = 3
# for _ in range(8):
#     timmy.pencolor(generate_rgb(), generate_rgb(), generate_rgb())
#     degree = 360/angles
#     timmy.seth(180 - degree)
#     for _ in range(angles):
#         timmy.forward(100)
#         timmy.right(degree)
#     angles += 1


### Random Walk###
# orientation = [90, 180, 270, 360]

# for _ in range(250):
#     timmy.pencolor(generate_rgb())
#     timmy.pensize(10)
#     timmy.speed(10)
#     timmy.seth(random.choice(orientation))
#     timmy.forward(30)


###Spirograph###
# timmy.speed(0)

# for _ in range(int(360/5)):
#     timmy.pencolor(generate_rgb())
#     timmy.circle(100)
#     timmy.left(5)


###Hirst painting###


colors = colorgram.extract('turtle/image.jpg', 25)
color_palette = []
for i in colors:
    color_palette.append((i.rgb.r, i.rgb.g, i.rgb.b))

color_palette.pop(0)
color_palette.pop(0)

print(color_palette)


screen = Screen()
screen.colormode(255)

timmy.penup()

position = [-250.00, -250.00]

for _ in range(10):
    timmy.goto(position)
    position = [position[0], position[1] + 50]
    for _ in range(10):
        timmy.dot(20, random.choice(color_palette))
        timmy.forward(50)
        


screen.exitonclick()
