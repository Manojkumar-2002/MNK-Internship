from turtle import Turtle, Screen

from spacy.ml.staticvectors import forward
from sympy.strategies.core import switch

from codes.spiral import right
import random

t = Turtle()
s = Screen()
t.speed(100)
color = ["red", "green", "yellow"]
t.shape("turtle")
t.penup()
t.goto(-28,-100)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(200)
t.end_fill()

for i in range(2):
    x = 360
    sides = 9
    t.penup()
    if i==0:
        t.goto(-100, 50)
    else:
        t.goto(100, 50)
    t.pendown()
    while sides > 2:
        angle = x / sides
        t.fillcolor(random.choice(color))
        t.begin_fill()
        for num in range(sides):
            t.backward(50)
            t.right(angle)
        sides -= 1
        t.end_fill()

t.penup()
t.goto(-90,-20)
t.pendown()
t.width(10)
t.right(58)
t.pencolor(random.choice(color))
t.circle(80, 120)
t.hideturtle()



s.exitonclick()
