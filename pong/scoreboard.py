from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Arial", 18, "normal")
FONT2 = ("Arial", 28, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.ht()
        self.penup()
        self.player1 = 0
        self.player2 = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Player1: {self.player1}\tPlayer2: {self.player2}", align=ALIGNMENT, font=FONT1)

    def increase_score(self, player):
        if player == "p1":
            self.player1 += 1
        else:
            self.player2 += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"      GAME OVER \nPLAYER 1 WINNER", align=ALIGNMENT, font=FONT2) if self.player1 > self.player2 else self.write(f"      GAME OVER \nPLAYER 2 WINNER", align=ALIGNMENT, font=FONT2)
