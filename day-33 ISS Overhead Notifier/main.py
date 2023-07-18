# ISS Overhead Notifier
# Munteanu Mihnea @ Mihnea03

import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 44.41117060612623
MY_LNG = 26.173720100090176

ISS_API_ENDPOINT = 'http://api.open-notify.org/iss-now.json'
SUN_API_ENDPOINT = 'https://api.sunrise-sunset.org/json'

EMAIL = "YOUR EMAIL"
PASS = "YOUR PASSWORD"
MSG = "Look up! ISS is waving to you!"

def send_mail():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=MSG)

def main():
    while True:
        # ISS Position
        response_iss = requests.get(url=ISS_API_ENDPOINT)
        response_iss.raise_for_status()
        data = response_iss.json()

        longitude = float(data["iss_position"]["longitude"])
        latitude = float(data["iss_position"]["latitude"])

        # Sunrise / Sunset
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LNG,
            "formatted": 0
        }
        
        response_sun = requests.get(url=SUN_API_ENDPOINT, params=parameters)    
        response_sun.raise_for_status()
        
        data_sun = response_sun.json()

        sunset = data_sun["results"]["sunset"]
        sunrise = data_sun["results"]["sunrise"]
        sunrise_hour = sunrise.split('T')[1].split(':')[0]
        sunset_hour = sunset.split('T')[1].split(':')[0]
        
        time_now = datetime.now()

        if abs(MY_LAT - latitude) < 5 and abs(MY_LNG - longitude) < 5 and time_now.hour < int(sunrise_hour) and time_now.hour > int(sunset_hour):
            send_mail()
        time.sleep(60)

if __name__ == '__main__':
    main()
