import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service ("C:/Users/SWATI/Desktop/webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_6j7dxt8smw_e&adgrpid=155259814793&hvpone=&hvptwo"
           "=&hvadid=676742245195&hvpos=&hvnetw=g&hvrand=12830884464333990947&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint"
           "=&hvlocphy=1007785&hvtargid=kwd-12692811&hydadcr=5624_2408770")
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']")))

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("mobile phones")
# time.sleep(2)
# driver.find_element(By.XPATH, "//div[@aria-label='mobile phones']").click()

lists = driver.find_elements(By.XPATH, "//div[@aria-label='mobile phones']")
for list in lists:
    if list.get_attribute('value') == "mobile phones":
     list.click()
    assert list.is_selected()
    break

driver.find_element(By.XPATH, "//img[@alt='Apple iPhone 15 (256 GB) - Green']").click()
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']"
                              "//input[@id='add-to-cart-button']").click()

driver.find_element(By.XPATH, "//input[@id='buy-now-button']").click()
driver.find_element(By.XPATH, "//input[@id='ap_email']").click()
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("+91 7774867878")
driver.find_element(By.XPATH, "//input[@id='continue']").click()
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("swati123")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

time.sleep(10)