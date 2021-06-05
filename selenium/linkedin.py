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

job_list = driver.find_elements_by_css_selector('.jobs-search-results .occludable-update')

for job in job_list:
    job.click()

    try:
        apply_button = driver.find_element_by_css_selector('.jobs-s-apply .jobs-apply-button')
        apply_button.click()
        next_button = driver.find_element_by_css_selector('footer button')
        next_button.click()
        cv_button = driver.find_elements_by_css_selector('footer button')[1]
        cv_button.click()
        follow_checker = driver.find_element_by_id('follow-company-checkbox')
        follow_checker.click()
        submit_button = driver.find_elements_by_css_selector('footer button')[1]
        submit_button.click()
        driver.find_element_by_css_selector('button').click()
    except:
        driver.find_element_by_css_selector('button').click()
        driver.find_elements_by_css_selector('footer button')[1]
        driver.find_elements_by_css_selector(".artdeco-modal--layer-confirmation button")[2].click()

driver.quit() 
