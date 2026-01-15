import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com")
time.sleep(1)
result='false'
try:
    result=driver.find_element(By.XPATH, "//img[@alt='Facebook1']").is_displayed()

except:
    print("Exception Handle")

print(result)