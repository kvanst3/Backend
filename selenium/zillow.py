from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup


req_headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
}
website = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
response = requests.get(url=website, headers=req_headers)
response.raise_for_status()

page = response.text
soup = BeautifulSoup(page, "html.parser")

listing = soup.find_all(class_="list-card-info")
ad_list = []

for ad in listing:
    try:
        address = ad.find(class_="list-card-addr").text
        price = ad.find(class_="list-card-price").text
        link = ad.select_one('a').get('href')

        flat = {
            "address": address,
            "price": price,
            "url": link,
        }
        ad_list.append(flat)
    except AttributeError:
        print(f"couldn't get ad at index: {listing.index(ad)}")


driver_path = "/home/k/Desktop/Python_projects/geckodriver"
url = 'https://docs.google.com/forms/d/e/1FAIpQLSc1Xg2V7BLVLDWs5PYWrufv3NrfjLeY_bVTfuKEkBsJBAQSHg/viewform?usp=sf_link'
driver = webdriver.Firefox(executable_path=driver_path)
time.sleep(2)
driver.get(url)

for ad in ad_list:
    input_fields = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    input_fields[0].send_keys(ad["address"])
    input_fields[1].send_keys(ad["price"])
    input_fields[2].send_keys(ad["url"])

    driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel").click()
    time.sleep(0.2)
    driver.find_element_by_css_selector('a').click()
    time.sleep(0.2)


driver.get(url)
print('r')

driver.quit()
