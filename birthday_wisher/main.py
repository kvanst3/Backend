import datetime as dt
import pandas as pd
from random import randint
import smtplib
from user_info import my_email, my_password

now = dt.datetime.now()

csv_content = pd.read_csv("birthday_wisher/birthdays.csv")
birthdays_data = csv_content.loc[(csv_content.day == now.day) & (csv_content.month == now.month)]
# could use .to_dict('records') but the following is clearer and generates less data, imo
birthday_bois = {row['name']: row['email'] for index, row in birthdays_data.iterrows()}

if len(birthday_bois) > 0:
    for name, email in birthday_bois.items():
        letter_num = randint(1, 3)
        with open(f"birthday_wisher/letter_templates/letter_{letter_num}.txt") as file:
            content = file.read()
            new_content = content.replace('[NAME]', name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday!\n\n{new_content}"
                )