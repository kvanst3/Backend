from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.update()

screen.listen()
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

game_on = True

while game_on:
    time.sleep(.1)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 5:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 5:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
