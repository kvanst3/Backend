from selenium import webdriver

chrome_driver_path = "/home/k/Desktop/Python_projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.fr/Instant-Pot-Autocuiseur-programmable-technologie/dp/B00OP26T4K/ref=pd_hr_sbs_1/262-7863249-2917012?pd_rd_w=vyITM&pf_rd_p=434c1bb1-8c71-4f67-9995-b53a01297836&pf_rd_r=1JFHGPD45Y52097B08GK&pd_rd_r=a807d307-bbd1-4b0c-b89d-e3e12331db38&pd_rd_wg=0hNRK&pd_rd_i=B00OP26T4K&th=1")
# price_element = driver.find_element_by_id("priceblock_ourprice")
# print(price_element.text)

driver.get('https://www.python.org/')
time_ele = driver.find_elements_by_css_selector('.event-widget time')
event_ele = driver.find_elements_by_css_selector('.event-widget li a')

event_dict = {}
for i, t in enumerate(time_ele):
    event_dict[i] = {
        "time": "2021-" + t.text,
        "event": event_ele[i].text,
        }

print(event_dict)

# driver.close() # closes the active tab
driver.quit() # quits the entire program