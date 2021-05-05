from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_counter_clockwise():
    tim.left(10)


def clear_drawing():
    tim.goto(0, 0)
    tim.clear()


tim.speed(0)
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(clear_drawing, "c")
screen.exitonclick()
