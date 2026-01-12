import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

plahld=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("placeholder")
print(plahld)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Pranav")
inptext=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("value")
print(inptext)
