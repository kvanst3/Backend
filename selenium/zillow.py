from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "/home/k/Desktop/Python_projects/geckodriver"
url = 'https://docs.google.com/forms/d/e/1FAIpQLSc1Xg2V7BLVLDWs5PYWrufv3NrfjLeY_bVTfuKEkBsJBAQSHg/viewform?usp=sf_link'
self.driver = webdriver.Firefox(executable_path=driver_path)

driver.get('url')
print('r')

driver.quit()
