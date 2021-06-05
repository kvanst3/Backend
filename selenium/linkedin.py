from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_driver_path = "/home/k/Desktop/Python_projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=91000005&keywords=python%20developer&location=Benelux")
time.sleep(1)
sign_in = driver.find_element_by_class_name('cta-modal__primary-btn')
sign_in.click()
time.sleep(1)

email_field = driver.find_element_by_id("username")
email_field.send_keys(os.environ.get('KV_EMAIL'))
password_field = driver.find_element_by_id("password")
password_field.send_keys(os.environ.get('LKDN_PW'))
password_field.send_keys(Keys.ENTER)
time.sleep(1)


driver.quit() 
