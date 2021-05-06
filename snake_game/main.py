from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.update()
screen.listen()

game_on = True

while game_on:
    screen.onkey(snake.turn_left, "a")
    screen.onkey(snake.turn_right, "d")
    time.sleep(.1)
    screen.update()
    snake.move()




screen.exitonclick()
