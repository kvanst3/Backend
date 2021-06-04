from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "/home/k/Desktop/Python_projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie = driver.find_element_by_id('bigCookie')
count = driver.find_element_by_id('cookies')

while True:
    try:
        upgrade = driver.find_element_by_css_selector('#upgrades .enabled')
        upgrade.click()
    except NoSuchElementException:
        print('no upgrades')
    try:
        products = driver.find_elements_by_css_selector('#products .product.enabled')
        pointer = driver.find_element_by_id('productOwned0')
        if pointer.text == '' or int(pointer.text) <= 10:
            for p in products:
                p.click()
        else:
            for p in products[1::]:
                p.click()
    except NoSuchElementException:
        print('no product')
    cookie.click()