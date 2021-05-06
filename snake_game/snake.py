from turtle import Turtle


class Snake():

    def __init__(self):
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        for _ in range(3):
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.1)
            snake.color("white")
            if len(self.segments) > 0:
                snake.goto(self.segments[-1].xcor() - 11, self.segments[-1].ycor())
            self.segments.append(snake)

    def move(self):
        # range(start=, stop=, step=) from 2 to(not including) 0, by -1
        for seg_i in range(len(self.segments) - 1, 0, - 1):
            self.segments[seg_i].goto(self.segments[seg_i - 1].pos())
        self.head.forward(10)

    def turn_left(self):
        self.head.left(90)

    def turn_right(self):
        self.head.right(90)
