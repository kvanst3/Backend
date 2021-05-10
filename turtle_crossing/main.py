from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time
        

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

player = Player()
screen.listen()
scoreboard = Scoreboard()
car_manager = Car()


game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    screen.onkey(player.move_forward, "Up")
    screen.onkey(player.move_backward, "Down")
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() >= 280:
        player.reset_pos()
        # prevent player movement while score flashes and turtle resets
        screen.onkey(None, "Up")
        screen.onkey(None, "Down")
        if scoreboard.level < 10:
            scoreboard.increase_level(screen)
            car_manager.increase_cars()
        else:
            screen.clear()
            scoreboard.win()
            screen.update()
            game_on = False



screen.exitonclick()
