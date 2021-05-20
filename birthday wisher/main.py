import smtplib
from user_info import my_email, my_password



connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, )