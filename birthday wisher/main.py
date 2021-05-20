from email import message
import smtplib
import datetime as dt
import random
from user_info import my_email, my_password

now  = dt.datetime.now()
# # make dt object
# date_of_birth = dt.datetime(year=1957, month=8, day=15)

if now.weekday() == 3:

    with open("birthday wisher/quotes.txt") as file:
        content = file.readlines()
        quotes = []
        for line in content:
            quotes.append(line.strip())

    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="charlesgroin@gmail.com",
            msg=f"Subject:Happy Birthday!\n\n{quote}"
        )