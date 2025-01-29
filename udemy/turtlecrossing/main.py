from turtle import Screen
from tur import Tur
from cars import Car
import time

from turtlecrossing.score import Score


class Main:
    def __init__(self):
        self.s = Screen()
        self.s.tracer(0)  # Turn off automatic screen updates for smoother animation
        self.s.bgcolor("black")
        self.s.setup(600, 700)
        self.score = Score(self.s)
        self.tur = Tur(self.s)  # Initialize player-controlled turtle
        self.car_manager = Car()  # Initialize cars
        self.game_mode()  # Start game loop and listen for input
        self.s.exitonclick()
        self.game_timer = 500

    def game_mode(self):
        self.s.listen()
        self.s.onkey(self.tur.move, "Up")  # Bind the "Up" key to the `move` method of `Tur`
        self.game_loop()

    def game_loop(self):

        result = self.car_manager.move(self.tur.turtle)  # Move all cars
        if result == "crash":
            self.score.game_over()
            return
        self.s.update()
        if self.tur.turtle.ycor() > 290:
            self.score.refresh()
            self.tur.refresh()
            if self.score.score == 4:
                self.score.check_winner()
                return

        self.s.ontimer(self.game_loop, 500)


main = Main()
