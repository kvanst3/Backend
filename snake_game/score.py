from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Arial", 18, "normal")
FONT2 = ("Arial", 28, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.ht()
        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except IOError:
            self.high_score = 0
        self.score = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\t High Score: {self.high_score}", align=ALIGNMENT, font=FONT1)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT2)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
