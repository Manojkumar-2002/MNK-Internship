import random
import time
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = self.find_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write(f"Score: {self.score}      High Score: {self.high_score} ", align="center", font=("Arial", 12, "italic"))

    def refresh(self):

        self.score += 1
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}      High Score: {self.high_score}", align="center", font=("Arial", 12, "italic"))

    def find_highscore(self):
        try:
            with open("highscore.txt", "r") as data:
                return int(data.read())
        except FileNotFoundError:
            return 0

    def new_highscore(self):
        with open("highscore.txt", 'w') as data:
            data.write(str(self.high_score))

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",
                   font=("Arial", 12, "italic"))
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_highscore()
        self.score = -1


