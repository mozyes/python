import datetime as dt
import smtplib
import random

MY_EMAIL = "email id here"
MY_PASSWORD = "password here"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        quotes_list = quote_file.readlines()
        quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="email id of other here",
            msg=f"Subject:Monday Motivation!\n\n{quote}"
        )
