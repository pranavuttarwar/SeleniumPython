import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/reg/?entry_point=login&next=")
result=driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").is_selected()
print(result)
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()
result=driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").is_selected()
print(result)
if result:
    print("Element is selected")
else:
    print("Element is not selected")
