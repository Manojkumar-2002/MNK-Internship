import os
from tkinter import *
from tkinter import ttk, messagebox, font
from tkinter.ttk import Combobox
import pandas as pd


from exceptions import (
    FileNotFoundError,
    DuplicateUsernameError,
    MissingFieldError,
    UserNotFoundError,
    NoDataFoundError,
)

window = Tk()
window.config(padx=10, pady=10)
window.title("Admin App")

frame = Frame(window)
frame.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")




update_id = 0
file = "users.csv"
last_id = 0

def show_error_message(message):
    messagebox.showerror("Error", message)
def show_success_message(message):
    messagebox.showinfo("Success",message)

def file_checker():
    if os.path.exists(file):
        return True
    else:
        raise FileNotFoundError(file)


def load_data():
    try:
        if file_checker():
            global last_id
            df = pd.read_csv(file)
            if not df.empty:
                last_id = df["ID"].to_list()[-1]
                return df
        return pd.DataFrame(columns=["ID", "Username", "Address", "JobDesignation"])
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        show_error_message(str(e))
        return pd.DataFrame(columns=["ID", "Username", "Address", "JobDesignation"])

def clear_data():
    user_name.delete(0, END)
    address.delete(0, END)
    job.delete(0, END)
    add_btn.config(text="Add")
    populate_filter_options()


def add_user_data():
    try:
        df = load_data()
        global last_id, update_id
        user = user_name.get()
        addr = address.get()
        job_des = job.get()

        if not user or not addr or not job_des:
            raise MissingFieldError()

        if update_id:
            if user in df.loc[df["ID"] != update_id, "Username"].to_list():
                raise DuplicateUsernameError(user)

            df.loc[df["ID"] == update_id, ["Username", "Address", "JobDesignation"]] = [user, addr,
                                                                                      job_des]
            df.to_csv(file, index=False)

            update_id = 0
            clear_data()
            show_success_message("Info updated successfully")
            return

        if user in df["Username"].to_list():
            raise DuplicateUsernameError(user)

        new_row = {
            "ID": last_id + 1,
            "Username": user,
            "Address": addr,
            "JobDesignation": job_des,
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(file, index=False)
        clear_data()
        show_success_message("User added successfully!")


    except (MissingFieldError, DuplicateUsernameError) as e:
        show_error_message(str(e))


def reset_filters():
    filter_address.set("Select Address")
    filter_job.set("Select Job Designation")
    populate_filter_options()
    listbox.delete(0, END)

def show_data(apply_filter=False):
    df = load_data()

    if apply_filter:
        address_filter = filter_address.get()
        job_filter = filter_job.get()

        mask = pd.Series(True, index=df.index)

        if address_filter != "Select Address":
            mask &= df["Address"] == address_filter

        if job_filter != "Select Job Designation":
            mask &= df["JobDesignation"] == job_filter

        df = df[mask]

    if not df.empty:
        users = df.to_dict(orient="records")
        listbox.delete(0, END)
        for user in users:
            us_id, us_name, user_addr, user_des = user.values()
            listbox.insert("end", f"{us_id}  {us_name} {user_addr} {user_des}")
    else:
        listbox.delete(0, END)
        listbox.insert("end", "No results match the filter criteria.")


def search_data():
    global update_id
    try:
        user_id = search.get()
        if not user_id.isdigit():
            raise ValueError("User ID must be a number.")

        user_id = int(user_id)
        df = load_data()
        if not df.empty:
            data = df[df["ID"] == user_id]
            if not data.empty:
                update_id = user_id
                user_name.delete(0, END)
                user_name.insert(0, data["Username"].iloc[0])
                address.delete(0, END)
                address.insert(0, data["Address"].iloc[0])
                job.delete(0, END)
                job.insert(0, data["JobDesignation"].iloc[0])
                search.delete(0, END)
                add_btn.config(text="Update")

            else:
                raise UserNotFoundError(user_id)
        else:
            raise NoDataFoundError()
    except (NoDataFoundError,UserNotFoundError, ValueError) as e:
        show_error_message(str(e))


def populate_filter_options():
    df = load_data()
    if not df.empty:
        addresses = ["Select Address"] + sorted(df["Address"].dropna().unique().tolist())
        jobs = ["Select Job Designation"] + sorted(df["JobDesignation"].dropna().unique().tolist())
        filter_address["values"] = addresses
        filter_job["values"] = jobs


# UI
underline_font = font.Font(family="Helvetica", size=12, weight="normal", underline=True)
add_title = Label(text="Add / Update Section",font=underline_font)
add_title.grid(row=0,column=0,columnspan=3)
user_label = Label(text="User Name")
user_label.grid(row=1, column=0, padx=5, pady=5)
user_name = Entry(width=40)
user_name.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

address_label = Label(text="Address")
address_label.grid(row=2, column=0, padx=5, pady=5)
address = Entry(width=40)
address.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


job_label = Label(text="Job Designation")
job_label.grid(row=3, column=0, padx=5, pady=5)
job = Entry(width=40)
job.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

clear_btn = Button(text="Cancel", command=clear_data, width=20)
clear_btn.grid(row=4, column=0, padx=5, pady=5)

add_btn = Button(text="Add", command=add_user_data, width=20)
add_btn.grid(row=4, column=2, padx=5, pady=5)


search_title = Label(text="Search and Update",font=underline_font)
search_title.grid(row=5,column=0,columnspan=3)
search_label = Label(text="Enter User Id")
search_label.grid(row=6, column=0, padx=5, pady=5)
search = Entry()
search.grid(row=6, column=1, padx=5, pady=5)
search_btn = Button(text="Search", command=search_data, bg="blue", fg="white",highlightthickness=0)
search_btn.grid(row=6, column=2, padx=5, pady=5)


filter_title = Label(text="Filter Section",font=underline_font)
filter_title.grid(row=7,column=0,columnspan=3)
filter_address = Combobox(width=18, state="readonly")
filter_address.grid(row=8, column=0, padx=5, pady=5, sticky="w")
filter_address.set("Select Address")
filter_address.bind("<<ComboboxSelected>>", lambda event: show_data(apply_filter=True))

filter_job = Combobox(width=18, state="readonly")
filter_job.grid(row=8, column=1, padx=5, pady=5, sticky="w")
filter_job.set("Select Job Designation")
filter_job.bind("<<ComboboxSelected>>", lambda event: show_data(apply_filter=True))

reset_filter_btn = Button(text="Reset Filter", command=reset_filters, bg="red", fg="white",highlightthickness=0)
reset_filter_btn.grid(row=8, column=2, padx=5, pady=5)

listbox = Listbox(frame, height=20, width=60)
listbox.grid(row=9, column=0,columnspan = 2,sticky="nsew", padx=5, pady=5)
scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
scrollbar.grid(row=9, column=2, sticky="ns", padx=5, pady=5)
listbox.config(yscrollcommand=scrollbar.set)


populate_filter_options()

window.mainloop()
