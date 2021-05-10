from turtle import Turtle
import time
ALIGNMENT = "left"
FONT1 = ("Arial", 18, "normal")
FONT1 = ("Arial", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-280, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT1)

    def increase_level(self, screen):
        self.level += 1
        for _ in range(3):
            self.clear()
            screen.update()
            time.sleep(0.3)
            self.update_scoreboard()
            screen.update()
            time.sleep(0.3)