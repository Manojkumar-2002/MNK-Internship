from tkinter import *



screen = Tk()
screen.title("Mile To Km")
screen.geometry("300x200")

screen.grid_columnconfigure(0, weight=1)

screen.grid_rowconfigure(0, weight=1)
screen.grid_rowconfigure(1, weight=1)
screen.grid_rowconfigure(2, weight=1)



def converter():
    try:
        ans = float(inp.get()) * 1.60934
        label.config(text=f"{ans:.2f} Km")
    except ValueError:
        label.config(text="Invalid Input")



label = Label(text=f"0 km", font=("Arial", 16))
label.grid(row=0, pady=10)

inp = Entry(font=("Arial", 14))
inp.grid(row=1, pady=10)



button = Button(text="Convert", command=converter, font=("Arial", 12))
button.grid(row=2,pady=10)

screen.mainloop()
