from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Arial", 18, "normal")
FONT2 = ("Arial", 28, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.ht()
        self.score = 0
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT1)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"GAME OVER\n     Score: {self.score}", align=ALIGNMENT, font=FONT2)
