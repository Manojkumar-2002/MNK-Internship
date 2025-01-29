from datetime import datetime
from dotenv import load_dotenv
import requests
import smtplib
import os
import pandas as pd
from email.message import EmailMessage

load_dotenv()
api = os.getenv("API")
params = {
    "lat":8.868054,
    "lon":78.027122,
    "cnt":4,
    "appid": api
}

res = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=params)
res.raise_for_status()
print(res.json())
data = res.json()["list"]
raining = False
temperature = []
humidity = []
for row in data:
    code = row["weather"][0]["id"]
    temp = row["main"]["temp"]
    hty = row["main"]["humidity"]
    temperature.append(temp)
    humidity.append(hty)
    if code < 700:
        raining = True

new_data = {
    "Temperature":temperature,
    "Humidity":humidity,
    "Date":datetime.now().date()
}

df = pd.DataFrame(new_data)
if os.path.exists("data.csv"):
    old_df = pd.read_csv("data.csv")
    data = pd.concat([old_df,df],ignore_index=True)
    data.to_csv("data.csv",index=False)

else:
    df.to_csv("data.csv",index=False)
print(df)

if not raining:
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER")
    password = os.getenv("PASSWORD")
    cc_emails = os.getenv("CC").split(",")
    subject = "It's not Raining"
    body = "No need to bring an Umbrella"
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Cc"] = ", ".join(cc_emails)
    msg["Subject"] = "It's not Raining"
    msg.set_content("There is no need to bring umbrella.")

    all_recipients = [receiver] + cc_emails

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            conn.send_message(msg,to_addrs=all_recipients)
    except Exception as e:
        print(f"Error occurred: {e}")