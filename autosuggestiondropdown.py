import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Users/vishw/Desktop/Personal/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "autosuggest").click()
driver.find_element(By.ID, "autosuggest").send_keys("In")
time.sleep(2)
list = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print("Number of countries:", len(list))
print("Number of countries:", len(list))

for country in list:
    if country.text == "India":
        country.click()
        break

time.sleep(10)