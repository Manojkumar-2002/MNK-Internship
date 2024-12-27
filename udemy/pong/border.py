from turtle import Turtle,Screen


class Border:
    def __init__(self,s):
        s.tracer(0)
        self.border = Turtle()
        self.border.color("white")
        self.border.penup()
        self.border.goto(-380, -280)
        self.border.pendown()
        for i in range(2):
            self.border.forward(760)
            self.border.left(90)
            self.border.forward(560)
            self.border.left(90)
        self.border.hideturtle()
        s.update()


