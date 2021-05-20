from email import message
import smtplib
from user_info import my_email, my_password



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="charlesgroin@gmail.com",
        msg="Subject:Happy Birthday!\n\nHello from python"
    )