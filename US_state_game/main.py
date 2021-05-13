import turtle
import pandas
from state import State
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.title("US_state_game")
image = "US_state_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = Scoreboard()

data = pandas.read_csv("US_state_game/50_states.csv")
game_on = True
while game_on:
    answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").capitalize()
    if answer in data.state.values:
        row = data[data.state == answer]
        State(row.state.values[0], row.x, row.y)
        data = data.drop(row.index)
        score.increase_score()


screen.exitonclick()