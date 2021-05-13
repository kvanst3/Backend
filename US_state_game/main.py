import turtle
import pandas
from state import State
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.title("US_state_game")
image = "US_state_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

data = pandas.read_csv("US_state_game/50_states.csv")
states = data.state.to_list()
game_on = True
while game_on:
    answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    if answer in states:
        row = data[data.state == answer]
        State(row.state.item(), row.x, row.y)
        data = data.drop(row.index)
        scoreboard.increase_score()
        if scoreboard.score >= 50:
            screen.clear()
            scoreboard.game_over()
            game_on = False
    elif answer == "Exit":
        data.state.to_csv("US_state_game/missed_answers.csv")
        game_on = False


screen.exitonclick()
