from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
t.shape("turtle")
t.speed(100)
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "indigo",
    "violet",
    "cyan",
    "hotpink"
]
# Function to fill the color for any shape
def fill_color(shape):
    color = random.choice(colors)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    shape(20)  # Call the shape function, e.g., circle with radius 20
    t.end_fill()

# Function to draw a square
def square():
    t.pencolor(random.choice(colors))
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)

# Function to draw diagrams with circles in a grid
def diagrams():
    y = -180
    while y < 180:
        t.penup()
        t.goto(-150, y)  # Move the turtle to the starting point for each row
        t.pendown()
        for i in range(6):  # Draw 6 circles in each row
            fill_color(t.circle)  # Use fill_color to fill each circle
            t.penup()
            t.forward(60)  # Move forward by 60 to position the next circle
            t.pendown()
        y += 60  # Move down by 60 for the next row

# Run the functions
square()  # Draw the square first
diagrams()  # Draw the diagrams (circle grid)

# Exit on click
s.exitonclick()
