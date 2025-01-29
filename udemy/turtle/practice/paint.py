from turtle import Turtle, Screen


class Paint:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.turtle()

    def turtle(self):
        t1 = Turtle()
        t1.shape("turtle")
        t1.turtlesize(2)
        t1.color("blue")
        t1.setheading(90)

        self.screen.listen()
        self.screen.onkey(lambda: t1.forward(10), "Up")
        self.screen.onkey(lambda: t1.backward(10), "Down")
        self.screen.onkey(lambda: t1.left(10), "Left")
        self.screen.onkey(lambda: t1.right(10), "Right")

        self.screen.mainloop()


paint = Paint()
