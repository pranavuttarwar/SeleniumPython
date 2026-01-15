import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
result=driver.find_element(By.XPATH,"//button[@type='submit']").is_enabled()
print("Facebook login: ",result)

time.sleep(2)
driver.get("http://instagram.com/")
result1=driver.find_element(By.XPATH,"//button[@type='submit']").is_enabled()
print("Instagram Login button",esult1)