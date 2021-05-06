from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.ht()
        self.score = 0
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()