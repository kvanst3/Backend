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

        self.down = self.driver.find_element_by_class_name('result-item-download').text.split('\n')[1]
        self.up = self.driver.find_element_by_class_name('result-item-upload').text.split('\n')[1]
        # self.driver.quit()

    def tweet_at_provider():
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        # #this needs to be adapted to ff (maybe)
        # email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        # password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        # email.send_keys(TWITTER_EMAIL)
        # password.send_keys(TWITTER_PASSWORD)
        # time.sleep(2)
        # password.send_keys(Keys.ENTER)

        # time.sleep(5)
        # tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        # tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        # tweet_compose.send_keys(tweet)
        # time.sleep(3)

        # tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        # tweet_button.click()

        # time.sleep(2)


ist = InternetSpeedTwitterBot()
ist.get_internet_speed()
print(ist.down)
print(ist.up)
