import time
from turtle import Turtle, Screen




class Snake:
    def __init__(self, s, food, score):
        self.food = food
        self.score = score
        self.up, self.down, self.right, self.left = 90, 270, 0, 180
        self.s = s
        self.s.tracer(0)
        self.turtles = self.create_turtle()

        self.s.listen()
        self.s.onkey(self.go_up, "Up")
        self.s.onkey(self.go_down, "Down")
        self.s.onkey(self.go_left, "Left")
        self.s.onkey(self.go_right, "Right")
        self.game_start()

    def create_turtle(self):
        turtle_list = []
        t_x = 0
        t_y = 0
        for i in range(3):
            t = Turtle("square")
            t.goto(t_x, t_y)
            t.color("white")
            t.penup()
            turtle_list.append(t)
            t_x -= 20
        return turtle_list

    def extend_turtle(self):
        t = Turtle("square")
        t.penup()
        last_turtle = self.turtles[-1]
        x_pos = last_turtle.xcor()
        y_pos = last_turtle.ycor()
        t.goto(x_pos, y_pos)
        t.color("white")
        self.turtles.append(t)

    def go_up(self):
        if self.turtles[0].heading() != self.down:
            self.turtles[0].setheading(self.up)

    def go_down(self):
        if self.turtles[0].heading() != self.up:
            self.turtles[0].setheading(self.down)

    def go_left(self):
        if self.turtles[0].heading() != self.right:
            self.turtles[0].setheading(self.left)

    def go_right(self):
        if self.turtles[0].heading() != self.left:
            self.turtles[0].setheading(self.right)

    def game_start(self):
        game_stat = True
        self.s.listen()
        while game_stat:
            self.s.update()
            head = self.turtles[0]
            time.sleep(0.1)

            # Move the rest of the snake
            for i in range(len(self.turtles)-1, 0, -1):
                prev_xcor = self.turtles[i-1].xcor()
                prev_ycor = self.turtles[i-1].ycor()
                self.turtles[i].goto(prev_xcor, prev_ycor)

            head.forward(20)

            # Check if snake eats food
            if head.distance(self.food) < 15:
                self.food.refresh()
                self.score.refresh()
                self.extend_turtle()

            # Check for collision with walls
            if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
                self.end_game()

            # Check for collision with itself
            for i in self.turtles[1:]:
                if head.distance(i) < 10:
                    self.end_game()

    def end_game(self):
        # Move all turtles off the screen
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.food.goto(1000,1000)
        self.score.game_over()
        self.s.update()
        time.sleep(3)

        # Ask for replay
        user_selection = self.s.textinput("User Input", "Do you want to replay (press enter)?")
        if user_selection is None:
            self.s.bye()

        # Reset game state
        self.score.refresh()
        self.food.refresh()
        self.turtles = self.create_turtle()
        self.game_start()
