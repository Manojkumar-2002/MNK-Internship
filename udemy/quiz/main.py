from ques_data import  questions
from ques import Ques

class Main:
    def __init__(self,questions):
        self.ques_no = 0
        self.score = 0

        for question in questions:
            self.text = question["question"]
            self.answer = question["answer"]
            ques = Ques(self.text,self.answer)
            self.ques_no += 1
            if ques.ask_question(self.ques_no):
                print("You are correct")
                self.score += 1
            else:
                print("you are wrong")
            ques.current_score(self.score,self.ques_no)
            print()
        print(f"Total Score: {self.score}/{self.ques_no}")


main = Main(questions)