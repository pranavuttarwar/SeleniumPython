#//tagname[@attributename='attributevalue']
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/")
#Enter UN
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Pranav")

#Enter PWD
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Pranav@123")

#Click Login
driver.find_element(By.XPATH,"//button[@class=' _aswp _aswr _aswu _asw_ _asx2']").click()
time.sleep(5)

driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Pranav")
driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("Pranav@123")
driver.find_element(By.XPATH,"//button[@name='login']").click()


time.sleep(5)

