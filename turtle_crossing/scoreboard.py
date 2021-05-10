from turtle import Turtle
import time
ALIGNMENT = "left"
ALIGNMENT2 = "center"
FONT1 = ("Arial", 18, "normal")
FONT2 = ("Arial", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-280, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.level < 10:
            self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT1)
        else:
            self.write("Final Level!", align=ALIGNMENT, font=FONT1)

    def increase_level(self, screen):
        self.level += 1
        # makes for score flashing - draws attention
        for _ in range(3):
            self.clear()
            screen.update()
            time.sleep(0.3)
            self.update_scoreboard()
            screen.update()
            time.sleep(0.3)

    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write("You Win!", align=ALIGNMENT2, font=FONT2)
