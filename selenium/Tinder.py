from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os


ff_driver_path = "/home/k/Desktop/Python_projects/chromedriver"

# options = Options()
# options.add_argument("-profile")
# options.add_argument("/home/k/.mozilla/firefox/whatever.selenium")
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# driver = webdriver.Firefox(executable_path=ff_driver_path, capabilities=firefox_capabilities, firefox_options=options)

driver = webdriver.Chrome(executable_path=ff_driver_path)


driver.get('https://tinder.com/app/recs')
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(.5)
main_window = driver.window_handles[0]
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(2)
login_window = driver.window_handles[1]
driver.switch_to_window(login_window)
time.sleep(1)
driver.find_elements_by_css_selector("div div div button")[1].click()
email_field = driver.find_element_by_id('email')
email_field.send_keys('ce_khaonation@hotmail.com')
pw_field = driver.find_element_by_id('pass')
pw_field.send_keys(os.environ.get('LKDN_PW').lower())
driver.find_element_by_id('loginbutton').click()
time.sleep(1)
driver.switch_to_window(main_window)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[1]').click()

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()

print('r')
driver.quit() 
