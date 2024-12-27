from turtle import Screen
from snake import Snake
from food import Food
from score import Score

class Main:
    def __init__(self):
        s = Screen()
        s.title("Snake Game")
        s.setup(600, 600)
        s.bgcolor("black")
        score = Score()
        food = Food(s)
        snake = Snake(s,food,score)
        s.exitonclick()


main = Main()

