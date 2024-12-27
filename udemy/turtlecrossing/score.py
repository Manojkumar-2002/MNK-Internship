import random
from turtle import Turtle


class Score(Turtle):
    def __init__(self,s):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.pendown()
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 12, "italic"))
        self.penup()
        self.goto(0, 280)
        self.pendown()
        s.update()

    def refresh(self):

            self.score += 1
            self.clear()
            self.penup()
            self.goto(0, 300)
            self.pendown()
            self.write(f"SCORE: {self.score}", align="center", font=("Arial", 12, "italic"))
            self.penup()
            self.goto(0, 280)
            self.pendown()

            return self.score

    def check_winner(self):
        self.goto(0,0)
        self.write(f"Your level is {self.score}", align="center", font=("Arial", 12, "italic"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Your level is {self.score}", align="center", font=("Arial", 12, "italic"))



