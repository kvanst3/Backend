from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:

    def __init__(self):
        driver_path = "/home/k/Desktop/Python_projects/geckodriver"
        self.driver = webdriver.Firefox(executable_path=driver_path)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        self.driver.find_element_by_id('_evidon-banner-acceptbutton').click()
        self.driver.find_element_by_class_name('start-text').click()
        time.sleep(60)
        # self.driver.find_element_by_css_selector('.modal .close-btn').click()
        self.down = self.driver.find_element_by_class_name('result-item-download').text.split('\n')[1]
        self.up = self.driver.find_element_by_class_name('result-item-upload').text.split('\n')[1]

    def tweet_at_provider():
        pass


ist = InternetSpeedTwitterBot()
ist.get_internet_speed()
print(ist.down)
print(ist.up)
