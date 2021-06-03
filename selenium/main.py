from selenium import webdriver

chrome_driver_path = "/home/k/Desktop/Python_projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# driver.close() # closes the active tab
# driver.quit() # quits the entire program