import smtplib

my_email = "myemail                 "
password = "#fromapppasswordhere"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="to email here",
        msg="Subject: testing python\n\nHow is this?"
    )
