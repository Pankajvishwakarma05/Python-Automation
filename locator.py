import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service ("C:/Users/SWATI/Desktop/webdriver/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# ID, CSS, XPATH, Class Name, Link Text

# XPATH  //tagname[@attribute='value']
# CSS  tagname[attribute='value']

driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Swati Shinde")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("swati@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("ss123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Female")
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("28/09/1998")
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
print("hello")

time.sleep(60)