import random
from turtle import Turtle


class Score(Turtle):
    def __init__(self,s):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.pendown()
        self.write(f"SCORE", align="center", font=("Arial", 12, "italic"))
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write(f"{self.score1} | {self.score2}", align="center", font=("Arial", 12, "italic"))
        s.update()

    def refresh(self,no):
        if no == 0:
            self.score2 += 1
            self.clear()
            self.penup()
            self.goto(0, 300)
            self.pendown()
            self.write(f"SCORE", align="center", font=("Arial", 12, "italic"))
            self.penup()
            self.goto(0, 280)
            self.pendown()
            self.write(f"{self.score1} | {self.score2}", align="center", font=("Arial", 12, "italic"))
            return self.score2
        else:
            self.score1 += 1
            self.clear()
            self.penup()
            self.goto(0, 300)
            self.pendown()
            self.write(f"SCORE", align="center", font=("Arial", 12, "italic"))
            self.penup()
            self.goto(0, 280)
            self.pendown()
            self.write(f"{self.score1} | {self.score2}", align="center", font=("Arial", 12, "italic"))
            return self.score1

    def check_winner(self,scorer):
        self.goto(0,0)
        self.write(f"Winner is {scorer}", align="center", font=("Arial", 12, "italic"))



