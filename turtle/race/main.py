from turtle import Turtle, Screen
import random


def race(turtles):
    winner = "none"
    while winner is "none":
        for t in turtles:
            t.forward(random.randint(1, 10))
            if t.xcor() >= 250:
                winner = t.pencolor()
    return winner


screen = Screen()
screen.setup(width=500, height=400)

turtle_names = ["am", "stram", "gram", "pic", "epic", "colegram"]
turtle_colors = ["red", "blue", "yellow", "green", "orange", "purple"]
turtle_coord = [-130, -80, -30, 20, 70, 120]

for i in range(len(turtle_names)):
    turtle_names[i] = Turtle()
    turtle_names[i].color(turtle_colors[i])
    turtle_names[i].penup()
    turtle_names[i].shape("turtle")
    turtle_names[i].goto(-250, turtle_coord[i])


player_bet = screen.textinput("Place a bet", "Which turtle will win? Enter a color:")
winning_turtle = race(turtle_names)
if winning_turtle == player_bet:
    screen.textinput((f"The {winning_turtle} turtle won!"), "You win your bet!")
else:
    screen.textinput((f"The {winning_turtle} turtle won!"), "You lost your bet...")

screen.exitonclick()