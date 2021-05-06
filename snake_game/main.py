from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.update()

screen.listen()
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

game_on = True

while game_on:
    time.sleep(.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.add_segment()




screen.exitonclick()
