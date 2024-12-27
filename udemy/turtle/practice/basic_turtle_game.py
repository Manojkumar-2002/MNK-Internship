from turtle import Turtle, Screen


class TurtleGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)

        self.turtle1()
        self.turtle2()

    def turtle1(self):
        t1 = Turtle()
        t1.shape("turtle")
        t1.turtlesize(2)
        t1.color("blue")
        t1.penup()
        t1.goto(-200, 0)
        t1.setheading(90)


        self.screen.onkey(lambda: t1.forward(10), "Up")
        self.screen.onkey(lambda: t1.backward(10), "Down")
        self.screen.onkey(lambda: t1.left(10), "Left")
        self.screen.onkey(lambda: t1.right(10), "Right")

    def turtle2(self):
        t2 = Turtle()
        t2.shape("turtle")
        t2.turtlesize(2)
        t2.color("red")
        t2.penup()
        t2.goto(200, 0)
        t2.setheading(90)


        self.screen.onkey(lambda: t2.forward(10), "w")
        self.screen.onkey(lambda: t2.backward(10), "s")
        self.screen.onkey(lambda: t2.left(10), "a")
        self.screen.onkey(lambda: t2.right(10), "d")




    def run(self):
        self.screen.listen()
        self.screen.mainloop()


# Create and run the game
game = TurtleGame()
game.run()
