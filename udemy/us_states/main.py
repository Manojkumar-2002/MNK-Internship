from turtle import Turtle, Screen
from check_state import StateChecker
from state_writer import StateWriter

class USStatesGame:
    def __init__(self, image_path):
        self.screen = Screen()
        self.screen.title("U.S States - 0 States Guessed")
        self.image_path = image_path
        self.screen.addshape(self.image_path)
        self.turtle = Turtle()
        self.turtle.shape(self.image_path)
        self.turtle.penup()
        self.state_checker = StateChecker("50_states.csv")
        self.state_writer = StateWriter()
        self.guessed_states = []
        self.correct_answers = []

    def get_user_input(self):
        prompt = f"Guess one state: ({len(self.correct_answers)} states guessed)"
        return self.screen.textinput("Guess the states of US", prompt)

    def check_state(self, user_input):
        if user_input.lower() in self.guessed_states:
            print(f"You already guessed {user_input}!")
            return False
        if self.state_checker.check_state_in_csv(user_input) and user_input.lower() not in self.correct_answers:
            print(f"{user_input} is a valid state!")
            self.guessed_states.append(user_input.lower())
            self.correct_answers.append(user_input.lower())
            self.place_state_on_map(user_input)
            self.update_title()
            return True
        elif user_input.lower() in self.correct_answers:
            print(f"You already guessed {user_input}!")
        else:
            print(f"{user_input} is not a valid state!")
        return False

    def place_state_on_map(self, state_name):
        coordinates = self.state_checker.get_state_coordinates(state_name)
        if coordinates:
            self.state_writer.place_state_on_map(state_name, coordinates)

    def update_title(self):
        """Update the title to reflect the number of states guessed correctly."""
        self.screen.title(f"U.S States - {len(self.correct_answers)} States Guessed")

    def display_game(self):
        print("Welcome to the US States Game!")
        while len(self.correct_answers) < 50:
            user_input = self.get_user_input()
            if user_input is None or len(self.correct_answers) == 50:
                self.state_writer.display_congratulations(len(self.guessed_states))
                break
            if self.check_state(user_input):
                print(f"Correct! You've guessed {len(self.correct_answers)} states.")
            if len(self.correct_answers) == 50:
                self.state_writer.display_congratulations(len(self.guessed_states))
                break
        self.screen.exitonclick()


game = USStatesGame("blank_states_img.gif")
game.display_game()
