from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = []

for _ in range(3):
    snake = Turtle()
    # snake.speed(1)
    snake.penup()
    snake.shape("square")
    snake.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.1)
    snake.color("white")
    if len(snakes) > 0:
        snake.goto(snakes[-1].xcor() - 11, snakes[-1].ycor())
    snakes.append(snake)

snake_head = snakes[0]

screen.update()
game_on = True

while game_on:
    time.sleep(.9)
    screen.update()
    last_segment_position = snake_head.pos()
    snake_head.forward(10)
    for seg in snakes[1:]:
        pos_before_movement = seg.pos()
        seg.goto(last_segment_position)
        last_segment_position = pos_before_movement

# screen.onkey()

screen.exitonclick()
