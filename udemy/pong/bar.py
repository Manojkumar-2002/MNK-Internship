from turtle import Turtle


class Bar:
    def __init__(self,s):
        self.bar1 = self.create_bar(0)
        self.bar2 = self.create_bar(1)
        s.update()

    def create_bar(self, no):
        colors = ["red", "green"]
        t = Turtle()
        t.penup()
        t.color(colors[no])
        t.shape("square")
        t.turtlesize(5, 1)
        if no == 0:
            t.goto(360,0)
        else:
            t.goto(-360,0)
        return t

    def go_up(self,bar):
        if bar.ycor() < 220:
            y = bar.ycor() + 20
            x = bar.xcor()
            bar.goto(x,y)


    def go_down(self,bar):
        if bar.ycor() > -220:
            y = bar.ycor() - 20
            x = bar.xcor()
            bar.goto(x, y)



