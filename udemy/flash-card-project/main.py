import os
import random
from tkinter import *
import pandas as pd

RED = "#e7305b"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
TIME = 3000
english = ''
french = ''
record = None


screen = Tk()
screen.config(padx = 20,pady=10,bg=BACKGROUND_COLOR)

def get_data():
    french_words_file = "data/french_words.csv"
    to_learn_file = "data/to_learn.csv"
    try:
        if os.path.exists(to_learn_file) and os.path.getsize(to_learn_file) > 2:
            df = pd.read_csv(to_learn_file).to_dict(orient = "records")
            return df
        elif os.path.exists(french_words_file):
            df = pd.read_csv(french_words_file).to_dict(orient="records")
            return df
        else:
            raise FileNotFoundError("Neither 'to_learn.csv' nor 'french_words.csv' exists.")
    except FileNotFoundError as e:
        print("File Not Found",e)
        df = []
        return df

records = get_data()

def show_english():
    global english
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=english,fill=YELLOW)
    canvas.itemconfig(img,image=b_img)

def show_data():
    global TIME,records
    if records:
        global english,french,record
        record = random.choice(records)
        french, english = record["French"], record["English"]
        canvas.itemconfig(title, text="French")
        canvas.itemconfig(word, text=french, fill=GREEN)
        canvas.itemconfig(img, image=f_img)
        screen.after(TIME, show_english)

def right():
    show_data()

    global records,record
    if record and records:
        records.remove(record)
        file = "data/to_learn.csv"
        df = pd.DataFrame(records)
        df.to_csv(file,index=False)
    else:
        canvas.itemconfig(title, text="")
        canvas.itemconfig(word, text="All words learned!", fill=RED)
        canvas.itemconfig(img, image=b_img)
        records = get_data()


def wrong():
    show_data()



f_img = PhotoImage(file="images/card_front.png")
b_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width = 800,height=550,bg = BACKGROUND_COLOR,highlightthickness=0)
img = canvas.create_image(400,275,image=f_img)
title = canvas.create_text(400,100,text="Title",fill=RED,font=(FONT_NAME, 20, 'bold'))
word = canvas.create_text(400,250,text="word",fill=GREEN,font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=0,column=0,columnspan = 2)




right_img = PhotoImage(file = "images/right.png")
right_btn = Button(image = right_img,command = right,highlightthickness=0)
right_btn.grid(row = 1,column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image= wrong_img,highlightthickness=0,command=wrong)
wrong_btn.grid(row = 1,column=1)

























screen.mainloop()