import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import pandas as pd

now = dt.datetime.now()
day = now.day
month = now.month

file = "people_data.csv"
df = pd.read_csv(file)
data = df[(df["month"]==month) & (df["day"]==day)]
if data.empty:
    print("No birthdays today!")
    exit()

load_dotenv()

try:
    mail = os.getenv("email")
    password = os.getenv("password")
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.starttls()
    conn.login(user=mail, password=password)

    for index, row in data.iterrows():

        name, receiver = row["name"], row["email"]
        subject = "Happy Birthday!"
        body = f"Dear {name},\n\nWishing you a very Happy Birthday!\n\nBest regards,\nYour Team"
        msg = f"Subject: {subject}\n\n{body}"
        conn.sendmail(from_addr=mail,to_addrs=receiver,msg=msg)
        print(f"Birthday email sent to {name} ({receiver})")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals():
        conn.quit()





