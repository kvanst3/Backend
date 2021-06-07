from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:

    def __init__(self):
        driver_path = "/home/k/Desktop/Python_projects/geckodriver"
        self.driver = webdriver.Firefox(executable_path=driver_path)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

    def tweet_at_provider():
        pass
