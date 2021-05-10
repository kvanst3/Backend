from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car import Car


def car_move():
    car.move_forward()
    screen.ontimer(car_move, 250)


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

player = Player()
screen.listen()
scoreboard = Scoreboard()
car = Car()


car_move()
game_on = True
while game_on:
    screen.update()
    screen.onkey(player.move_forward, "w")
    if player.ycor() >= 280:
        player.reset_pos()
        screen.onkey(None, "w")
        scoreboard.increase_level(screen)
        #increase car speed



screen.exitonclick()
