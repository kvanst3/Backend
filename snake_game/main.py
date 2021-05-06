from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


snakes = []

for _ in range(3):
    snake = Turtle()
    snake.penup()
    snake.shape("square")
    snake.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.1)
    snake.color("white")
    if len(snakes) > 0:
        snake.goto(snakes[-1].xcor() - 11, snakes[-1].ycor())
    snakes.append(snake)



screen.exitonclick()
