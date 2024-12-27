from turtle import Turtle
import random

class StateWriter:
    def __init__(self):
        self.state_turtles = []

    def place_state_on_map(self, state_name, coordinates):
        state_turtle = Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(coordinates[0], coordinates[1])

        state_turtle.color(self.generate_random_color())

        state_turtle.write(state_name.title(), align="right", font=("Arial", 8, "normal"))

        self.state_turtles.append(state_turtle)

    def generate_random_color(self):
        colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]
        return random.choice(colors)

    def display_congratulations(self,length):
        """Display the congratulations message in large text at the center of the screen."""
        congrats_turtle = Turtle()
        congrats_turtle.penup()
        congrats_turtle.hideturtle()
        congrats_turtle.goto(0, 0)
        congrats_turtle.color("green")
        congrats_turtle.write(f"Congratulations! You've guessed {length} states!", align="center", font=("Arial", 24, "bold"))
