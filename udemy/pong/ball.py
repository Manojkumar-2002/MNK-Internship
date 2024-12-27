import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self,s):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        self.x = 10
        self.y = 10
        s.update()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1




