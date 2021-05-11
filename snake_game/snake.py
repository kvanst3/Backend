from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]

    def add_segment(self):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0)
        segment.color("white")
        if len(self.segments) > 0:
            if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
                segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor() - 11)
            else:
                segment.goto(self.segments[-1].xcor() - 11, self.segments[-1].ycor())
        self.segments.append(segment)

    def generate_snake(self):
        for _ in range(3):
            self.add_segment()

    def move(self):
        # range(start=, stop=, step=) from 2 to(not including) 0, by -1
        for seg_i in range(len(self.segments) - 1, 0, - 1):
            self.segments[seg_i].goto(self.segments[seg_i - 1].pos())
        self.head.forward(10)

    def turn_left(self):
        self.head.left(90)

    def turn_right(self):
        self.head.right(90)

    def reset(self):
        for seg in self.segments:
            seg.ht()
        self.segments.clear()
        self.generate_snake()
        self.head = self.segments[0]