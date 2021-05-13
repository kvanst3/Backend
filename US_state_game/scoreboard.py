from turtle import Turtle, update


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 300)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}/50",font=28, align="left")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
