from turtle import Turtle, Screen
import random


class TurtleGame:
    def __init__(self):
        self.s = Screen()
        self.t = Turtle()
        self.t.hideturtle()
        self.user_selection = self.s.textinput("User Input", "Which turtle will win the race (blue or red or green) default(blue) ")
        if self.user_selection is None or self.user_selection == "":
            self.user_selection = "blue"
        self.finish()
        self.t1 = self.create_turtle("red", -100, -100)
        self.t2 = self.create_turtle("blue", 100, -100)
        self.t3 = self.create_turtle("green",0, -100)
        self.finish_line = 250
        self.race_decision = self.race()
        self.check_winner()
        self.s.mainloop()

    def finish(self):
        t = Turtle()
        t.penup()
        t.goto(-150, 250)
        t.pendown()
        t.setheading(0)
        t.forward(300)
        t.hideturtle()

    def create_turtle(self, color, x, y):
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.turtlesize(2)
        t.speed(1)
        t.pensize(5)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(90)
        return t
    def race(self):
        while True:
            self.move_turtle(self.t1)
            self.move_turtle(self.t2)
            self.move_turtle(self.t3)

            if self.t1.ycor() >= self.finish_line:
                print(f"red turtle is the winner")
                return "red"
            elif self.t2.ycor() >= self.finish_line:
                print(f"blue turtle is the winner")
                return "blue"
            elif self.t3.ycor() >= self.finish_line:
                print(f"green turtle is the winner")
                return "green"

    def move_turtle(self,turtle):
        pace = random.randint(1,10)
        turtle.forward(pace)

    def check_winner(self):
        self.t.penup()
        self.t.goto(-50,-200)
        self.t.pendown()
        if self.user_selection == self.race_decision:
            self.t.write(f"you won {self.user_selection} turtle won the race", align="center", font=("Arial", 18, "italic"))
        else:
            self.t.write(f"You have lost! {self.user_selection} turtle has lost!", align="center",font=("Arial", 18, "italic"))


turtle = TurtleGame()
