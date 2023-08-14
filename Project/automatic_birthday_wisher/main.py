import smtplib
import random
import datetime as dt
import pandas

MY_EMAIL = "Email here"
PASSWORD = "password here"

birthday = pandas.read_csv("birthdays.csv")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

hday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday.iterrows()}

if today_tuple in hday_dict:
    birthday_person = hday_dict[today_tuple]
    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,  PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
