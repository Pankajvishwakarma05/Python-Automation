import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Users/vishw/Desktop/Personal/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/gmail/about/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//body/header[1]/div[1]/div[1]/div[1]/a[3]/span[2]").click()
element = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
driver.find_element(By.ID, "firstName").send_keys("Pankaj")
driver.find_element(By.ID, "lastName").send_keys("Vishwakarma")
driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d']").click()
wait.until(EC.visibility_of_element_located((By.ID, "month")))
# driver.find_element(By.ID, "month").click()
month = Select(driver.find_element(By.ID, "month"))
# dropdown.select_by_visible_text("September")
month.select_by_index(9)
driver.find_element(By.ID, "day").click()
driver.find_element(By.ID, "day").send_keys("5")
driver.find_element(By.ID, "year").click()
driver.find_element(By.ID, "year").send_keys("1997")
dropdown = Select(driver.find_element(By.ID, "gender"))
dropdown.select_by_visible_text("Male")
# driver.find_element(By.ID, "gender").click()

driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d']").click()
time.sleep(10)

