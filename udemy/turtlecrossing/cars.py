import random
from turtle import Turtle

class Car:
    def __init__(self):

        self.cars = []
        colors = ["red", "green", "blue", "yellow", "violet"]
        self.car_choice = list(range(280, 1000, 20))

        for i in range(36):
            car = Turtle("square")
            car.penup()
            car.color(random.choice(colors))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(self.car_choice[i], random.randint(-270, 280))
            car.setheading(180)  # Face left
            self.cars.append(car)

    def move(self,turtle):
        for car in self.cars:
            car.forward(20)
            if abs(turtle.xcor() - car.xcor()) < 18 and abs(turtle.ycor() - car.ycor()) < 18:
                return "crash"

            if car.xcor() < -300:
                car.goto(random.choice(self.car_choice), random.randint(-260, 280))
