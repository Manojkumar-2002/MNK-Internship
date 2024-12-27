import os
import pandas as pd
import string
import random
from tkinter import *
from tkinter import messagebox

# Initialize the main screen
screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20, bg="#f7f5dd")

# Password generator
def pass_generator():
    characters = string.ascii_letters + string.digits + string.punctuation
    try:
        password = "".join(random.choice(characters) for _ in range(12))
        password_inp.delete(0, END)
        password_inp.insert(0, password)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Get input data
def get_data():
    web = web_inp.get().strip()
    email = email_inp.get().strip()
    password = password_inp.get().strip()
    return web, email, password

# Clear input fields
def delete_data():
    web_inp.delete(0, END)
    email_inp.delete(0, END)
    password_inp.delete(0, END)

# Add or update data in the JSON file using pandas
def add_data():
    web_data, email_data, pass_data = get_data()

    if not web_data or not email_data or not pass_data:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    json_file = "data.json"

    try:
        # Load existing data or create a new DataFrame
        if os.path.exists(json_file):
            df = pd.read_json(json_file)
        else:
            df = pd.DataFrame(columns=["website", "email", "password"])

        # Check if the website already exists
        if not df[df["website"] == web_data].empty:
            df.loc[df["website"] == web_data, ["email", "password"]] = [email_data, pass_data]
            messagebox.showinfo("Success", "Data updated successfully!")
        else:
            # Add a new entry
            new_entry = pd.DataFrame([{"website": web_data, "email": email_data, "password": pass_data}])
            df = pd.concat([df, new_entry], ignore_index=True)
            messagebox.showinfo("Success", "Data added successfully!")

        # Save the updated data
        df.to_json(json_file, orient="records", indent=4)
        delete_data()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Search for data in the JSON file using pandas
def search():
    web_data = web_inp.get().strip()
    json_file = "data.json"

    if not web_data:
        messagebox.showerror("Error", "Please enter a website to search.")
        return

    try:
        if os.path.exists(json_file):
            df = pd.read_json(json_file)

            # Filter the DataFrame for the specified website
            result = df[df["website"] == web_data]

            if not result.empty:
                email = result.iloc[0]["email"]
                password = result.iloc[0]["password"]
                email_inp.delete(0, END)
                email_inp.insert(0, email)
                password_inp.delete(0, END)
                password_inp.insert(0, password)
                messagebox.showinfo("Data Found", f"Email: {email}\nPassword: {password}\nYou can update the data using the Add button.")
            else:
                messagebox.showerror("Error", "No data found for the specified website.")
        else:
            messagebox.showerror("Error", "No data file found. Please add data first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# UI Setup
canvas = Canvas(width=200, height=200, bg="#f7f5dd", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=("Arial", 12, "bold"), bg="#f7f5dd", fg="#333")
website_label.grid(row=1, column=0, pady=5)

web_inp = Entry(width=35)
web_inp.grid(row=1, column=1, pady=5)
web_inp.focus()

search_btn = Button(text="Search", command=search, bg="#2196f3", fg="white", font=("Arial", 12, "bold"))
search_btn.grid(row=1, column=2, pady=5)

email_label = Label(text="Email", font=("Arial", 12, "bold"), bg="#f7f5dd", fg="#333")
email_label.grid(row=2, column=0, pady=5)

email_inp = Entry(width=35)
email_inp.grid(row=2, column=1, pady=5)

password_label = Label(text="Password", font=("Arial", 12, "bold"), bg="#f7f5dd", fg="#333")
password_label.grid(row=3, column=0, pady=5)

password_inp = Entry(width=35)
password_inp.grid(row=3, column=1, pady=5)

pass_generator_btn = Button(text="Generate", command=pass_generator, bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
pass_generator_btn.grid(row=3, column=2, pady=5)

add_btn = Button(text="Add", command=add_data, width=36, bg="#2196f3", fg="white", font=("Arial", 12, "bold"))
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

screen.mainloop()
