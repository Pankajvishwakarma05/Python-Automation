import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_obj = Service("C:/Users/vishw/Desktop/Personal/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)      # wait.until(EC.visibility_of_element_located((By.ID, "tab_admin_users")))
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")))
driver.find_element(By.CSS_SELECTOR, "a[class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='firstname']")))
driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Pankaj")
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Vishwakarma")
driver.find_element(By.CSS_SELECTOR, "input[name='reg_email__']").send_keys("8788218107")
dropdown = Select(driver.find_element(By.ID, "day"))
dropdown.select_by_visible_text("30")
dropdown.select_by_index(29)




time.sleep(10)
