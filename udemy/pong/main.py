import random
import time
from turtle import Turtle,Screen

from border import Border
from score import Score
from bar import Bar
from ball import Ball


class Main:
    def __init__(self):
        s = Screen()
        s.bgcolor("black")
        s.setup(800,700)
        Border(s)
        self.bar = Bar(s)
        print(self.bar.bar1.pos())
        self.ball = Ball(s)
        self.score = Score(s)
        self.game_mode(s)
        s.exitonclick()

    def game_mode(self,s):
        game_stat = True
        s.listen()
        while game_stat:
            time.sleep(0.1)
            s.update()
            s.onkey(lambda: self.bar.go_up(self.bar.bar1), "Up")
            s.onkey(lambda: self.bar.go_down(self.bar.bar1), "Down")
            s.onkey(lambda: self.bar.go_up(self.bar.bar2), "w")
            s.onkey(lambda: self.bar.go_down(self.bar.bar2), "s")
            self.ball.move()
            if self.ball.ycor() >= 270 or self.ball.ycor() <= -270:
                self.ball.bounce_y()

            if self.ball.distance(self.bar.bar1) < 70 and self.ball.xcor() > 348 or self.ball.distance(self.bar.bar2) < 70 and self.ball.xcor() < -348:
                self.ball.bounce_x()

            if self.ball.xcor() > 380:
                score1 = self.score.refresh(1)
                self.ball.goto(0,random.randint(-240,240))
                self.ball.bounce_x()
                if score1 >= 5:
                    self.score.check_winner("Green")
                    game_stat = False

            elif self.ball.xcor() <-380:
                score2 = self.score.refresh(0)
                self.ball.goto(0, random.randint(-240, 240))
                self.ball.bounce_x()
                if score2 >= 5:
                    self.score.check_winner("Red")
                    game_stat = False









main =Main()