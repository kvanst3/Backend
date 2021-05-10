from turtle import Turtle
import random
COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown']


class Car():

    def __init__(self):
        super().__init__()
        self.cars = []
        self.generation_chance = 50

    def create_car(self):
        if random.randint(1, self.generation_chance) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=0.8, stretch_len=2, outline=0)
            random_y = random.randint(-240, 240)
            new_car.goto((-320, random_y))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(2)

    def increase_cars(self):
        if self.generation_chance > 5:
            self.generation_chance -= 5
