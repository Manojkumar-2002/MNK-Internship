import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
