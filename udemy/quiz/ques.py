class Ques:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

    def ask_question(self,ques_no):
        user_ans = input(f"Q.no {ques_no}: {self.text}:(True/False): ")
        return bool(user_ans) == self.answer

    def current_score(self,score,ques_no):
        print(f"Current Score: {score}/{ques_no}")




