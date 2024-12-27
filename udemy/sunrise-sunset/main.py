import requests
import datetime as dt
import smtplib
import os


from dotenv import load_dotenv
load_dotenv()

hour = dt.datetime.now().hour
lat=-4.178590
lng=-38.130650
lat_lng = {
    "lat":lat,
    "lng":lng,
    "formatted":0
}
# sunrise time and sunset time
res = requests.get("https://api.sunrise-sunset.org/json",params=lat_lng)
data = res.json()["results"]
sun_rise = int(data["sunrise"].split('T')[1].split(':')[0])
sunset = int(data["sunset"].split('T')[1].split(':')[0])


# ISS long and lat
iss_res = requests.get("http://api.open-notify.org/iss-now.json")
iss_long = float(iss_res.json()['iss_position']['longitude'])
iss_lat = float(iss_res.json()['iss_position']['latitude'])

print("sunrise:",sun_rise,"sunset:",sunset)
print("current hour:",hour)
print("ISS lat",iss_lat,"ISS long",iss_long)

def night_check():
    if sun_rise > hour > sunset:
        return True

def iss_pos_checker():
    if  lat - 5 < iss_lat < lat + 5 and lat - 5 < iss_long < lat + 5:
        return True


if night_check() and iss_pos_checker():
    mail = os.getenv("email")
    password = os.getenv("password")
    receiver = os.getenv("rec_mail")

    try:
        conn = smtplib.SMTP("smtp.gmail.com", 587)
        conn.starttls()
        conn.login(user=mail, password=password)
        subject = "Look Above"
        body = f"The ISS is above you in the sky."
        msg = f"Subject: {subject}\n\n{body}"
        conn.sendmail(from_addr=mail, to_addrs=receiver, msg=msg)
    except Exception as e:
            print(f"An error occurred: {e}")

    finally:
        if 'conn' in locals():
            conn.quit()