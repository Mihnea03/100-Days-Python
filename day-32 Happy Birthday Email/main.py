# Happy Birthday Email
# Munteanu Mihnea @ Mihnea03

import smtplib
import datetime as dt
import pandas as pd

email = "YOUR EMAIL"
password = "YOUR PASSWORD"

def main():
    data = pd.read_csv("birthdays.csv")
    now = dt.datetime.now()

    for (_, person) in data.iterrows():
        if now.month == person.month and now.day == person.day:
            with open("letter.txt", 'r') as letter_file:
                message = letter_file.read()
            message = message.replace("[NAME]", person["name"])

            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email, to_addrs=person.email, msg=message)
    return

if __name__ == '__main__':
    main()
