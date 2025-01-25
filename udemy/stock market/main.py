import os
from dotenv import load_dotenv
import requests
import smtplib
from email.message import EmailMessage


load_dotenv()
stock_api = os.getenv("STOCK_API")
news_api = os.getenv("NEWS_API")
sender = os.getenv("SENDER")
receiver = os.getenv("RECEIVER")
password = os.getenv("PASSWORD")
cc_emails = os.getenv("CC").split(",")


def find_stock_percent():
    stock_params = {
        "apikey": stock_api,
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM"
    }
    res = requests.get("https://www.alphavantage.co/query", params=stock_params)
    data = [val for key, val in res.json()["Time Series (Daily)"].items()]
    today_stock_price = float(data[0]["4. close"])
    yes_stock_price = float(data[1]["4. close"])
    diff = today_stock_price - yes_stock_price
    print(diff)
    percent = (abs(diff) / today_stock_price) * 100
    print(yes_stock_price, today_stock_price, percent)
    if diff > 0:
        message = f"IBM price went up by {percent} %"
    elif diff < 0:
        message = f"IBM price went down by {percent} %"
    else:
        message = f"No changes in IBM price %"

    return message

def find_news_art():
    new_params = {
        "q": "IBM",
        "apiKey": news_api
    }
    news_res = requests.get("https://newsapi.org/v2/everything", params=new_params)
    articles = news_res.json()["articles"][:3]
    processed_data = []

    for article in articles:
        title = article.get("title", "No title available").strip()
        description = article.get("description", "No description available").strip()

        if "Removed" in title or "Removed" in description:
            print("Skipping removed content...")
            continue

        title = title.replace("\u200b", "")
        description = description.replace("\u200b", "")

        print(f"Processed Headline: {title}")
        print(f"Processed Description: {description}")

        processed_data.append({"headline": title, "description": description})

    return processed_data

news = find_news_art()
stock = find_stock_percent()
print(news,stock)

with smtplib.SMTP("smtp.gmail.com",587) as conn:
    conn.starttls()
    conn.login(sender,password)
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Cc"] = ", ".join(cc_emails)
    msg["Subject"] = f"{stock}"

    all_recipients = [receiver] + cc_emails


    for i in news:
        message = f"Headline: {i['headline']}\nDescription: {i['description']}"
        msg.set_content(message)
        conn.send_message(msg,from_addr=sender,to_addrs=all_recipients)