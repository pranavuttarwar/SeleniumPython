import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
Text=driver.find_element(By.XPATH,"//a[contains(text(),'Forgotten password?')]").text

print(Text)

time.sleep(2)