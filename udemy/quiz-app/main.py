from tkinter import *
from tkinter import messagebox, simpledialog
import random

from high_score import Highscore
from questions import Questions
import html
THEME_COLOR = "#375362"

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Application")
        self.window.config(padx=20, pady=20,bg = "#375362")

        self.ques = Questions()
        self.questions = self.ques.get_questions()

        self.high_scorers = Highscore()
        self.high_scorer,self.high_score = self.high_scorers.get_high_score()
        self.leaderboard = self.high_scorers.get_leaderboard()

        self.ques_no = 1
        self.current_ans = ""
        self.current_ques = None
        self.score = 0
        self.user_name = ""

        self.high_scorer_label = Label(
            text=f"High Scorer: {self.high_scorer}",
            font=("Arial", 14),
            anchor="center",
            padx=10,
            pady=10,
            fg ="#A8FFCE",
            bg="#375362"
        )
        self.high_scorer_label.grid(row=0, column=0, pady=10)

        self.high_score_label = Label(
            text=f"High Score = {self.high_score}",
            font=("Arial", 14),
            anchor="center",
            padx=10,
            pady=10,
            fg ="#A8FFCE",
            bg="#375362"
        )
        self.high_score_label.grid(row=0, column=1, pady=10)
        self.score_label = Label(
            text="Score = 0",
            font=("Arial", 14),
            anchor="center",
            padx=10,
            pady=10,
            fg ="#A8FFCE",
            bg="#375362"
        )
        self.score_label.grid(row=0, column=2, pady=10)

        self.ques_label = Label(
            text="",
            font=("Arial", 18, "italic"),
            wraplength=400,
            padx=10,
            pady=10,
            width=50,
            fg = "#FFD700",
            bg="#375362",
            highlightthickness=1,
            highlightbackground="#FFFAFA",
            highlightcolor="#FFFFFF"
        )
        self.ques_label.grid(row=1, column=0, columnspan=3, pady=20)

        right_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(
            image=right_img, command=self.right, highlightthickness=0, padx=20, pady=20
        )
        self.right_btn.image = right_img
        self.right_btn.grid(row=2, column=0, padx=10)

        self.choose_label = Label(
            text="Click ✓ for True or ✗ for False",
            font=("Arial", 16, "bold"),
            padx=10,
            pady=10,
            fg = "#B3D9FF",
            bg="#375362"
        )
        self.choose_label.grid(row=2, column=1, pady=20)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(
            image=wrong_img, command=self.wrong, highlightthickness=0, padx=20, pady=20
        )
        self.wrong_btn.image = wrong_img
        self.wrong_btn.grid(row=2, column=2, padx=10)
        self.get_user_name()

        self.canvas = Canvas(width=400,bg=THEME_COLOR)
        self.canvas.grid(row=0,column=3,rowspan=3,padx=5)
        self.create_leaderboard()
        self.ask_ques()

        self.window.mainloop()

    def get_user_name(self):
        username = simpledialog.askstring("User Name", "Enter your name:")
        self.user_name = username
        if not username:
            self.user_name = "Guest"
        text = f"Quiz Application   User: {self.user_name}"
        self.window.title(text)

    def ask_ques(self):
        self.current_ques = random.choice(self.questions)
        text = html.unescape(self.current_ques["question"])
        self.current_ans = self.current_ques["correct_answer"]
        self.ques_label.config(text=f"{self.ques_no}: {text}")

    def right(self):
        print(self.current_ques, self.current_ans)
        if self.current_ans == "True":
            self.display_ans("The answer is True")
            self.score += 1
        else:
            self.display_err("The answer is False")
        self.ask_next()

    def wrong(self):
        if not self.current_ans == "False":
            self.display_ans("The answer is False")
            self.score += 1
        else:
            self.display_err("The answer is True")
        self.ask_next()

    def ask_next(self):
        if self.questions:
            self.questions.remove(self.current_ques)
            print(len(self.questions))
            if len(self.questions) > 0:
                self.ques_no += 1
                self.score_label.config(text=f"Score = {self.score}")
                self.ask_ques()
            else:
                self.clear_data()
        else:
            self.clear_data()

    def clear_data(self):
        self.ques_label.config(text="You have completed")
        self.right_btn.config(state="disabled")
        self.wrong_btn.config(state="disabled")
        if self.score > self.high_score:
            messagebox.showinfo("", "You are the new high scorer")
            self.high_scorers.set_high_score(self.user_name, self.score)


    def display_ans(self, msg):
        messagebox.showinfo("You are right", msg)

    def display_err(self, msg):
        messagebox.showerror("You are wrong", msg)

    def create_leaderboard(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 20, text="Leaderboard", font=("Arial", 16, "bold"),fill="yellow")
        self.canvas.create_text(200, 50, text=f"Ind     Users     Scores", font=("Arial", 12,"bold"), anchor="center")

        y_offset = 70
        for idx, entry in enumerate(self.leaderboard, start=1):
            text = f"  {idx}       {entry['users']}       {entry['scores']} points"
            self.canvas.create_text(200, y_offset, text=text, font=("Arial", 12), anchor="center",fill="white")
            y_offset += 30


main = Main()
