import requests
from bs4 import BeautifulSoup
import smtplib
import os

website = 'https://www.amazon.fr/Instant-Pot-Autocuiseur-programmable-technologie/dp/B00OP26T4K/ref=pd_hr_sbs_1/262-7863249-2917012?pd_rd_w=vyITM&pf_rd_p=434c1bb1-8c71-4f67-9995-b53a01297836&pf_rd_r=1JFHGPD45Y52097B08GK&pd_rd_r=a807d307-bbd1-4b0c-b89d-e3e12331db38&pd_rd_wg=0hNRK&pd_rd_i=B00OP26T4K&th=1'
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
}
response = requests.get(website, headers=headers)
response.raise_for_status
page = response.text

soup = BeautifulSoup(page, "lxml")
price = soup.select_one('#priceblock_ourprice').getText().split()[0]
print(price)

my_email = os.environ.get("INDI_EMAIL")
my_pw = os.environ.get('INDI_PW')

price = '79,78'

if float(price) < 85:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"the thing is at {price}€ go check it out on {website}"
        )