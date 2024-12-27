from turtle import Turtle



class Tur:
    def __init__(self,s):
        self.turtle = self.create_turtle()
        s.update()

    def create_turtle(self):
        t = Turtle("turtle")
        t.color("white")
        t.penup()
        t.goto(-300,300)
        t.pendown()
        t.forward(600)
        t.penup()
        t.goto(0, -280)
        t.setheading(90)
        return t
    def refresh(self):
        self.turtle.penup()
        self.turtle.goto(0, -290)
        self.turtle.setheading(90)

    def move(self):
        self.turtle.forward(20)


