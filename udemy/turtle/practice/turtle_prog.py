import turtle


screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(50)
t.pensize(4)


# outer shadow
t.penup()
t.color("grey")
t.goto(0,-110)
t.pendown()
t.begin_fill()
t.circle(160)
t.end_fill()


# inner circle
t.penup()
t.color("yellow")
t.goto(0,-100)
t.pendown()
t.begin_fill()
t.circle(150)
t.end_fill()

# left eye shadow
t.penup()
t.goto(-45,42)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(28)
t.end_fill()

# left eye
t.penup()
t.goto(-45,45)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()


# right eye shadow
t.penup()
t.goto(45,42)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(28)
t.end_fill()

# right eye
t.penup()
t.goto(45,45)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()




# mouth
t.penup()
t.width(4)
t.goto(-40,-5)
t.pendown()
t.color("black")
t.setheading(-60)
t.circle(50, 120)
t.hideturtle()






screen.exitonclick()


