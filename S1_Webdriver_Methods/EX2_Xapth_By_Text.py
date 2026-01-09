#//tagname[text()='value'] --> Syntax
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#driver.get("https://www.instagram.com/")
#driver.maximize_window()
#time.sleep(2)
#driver.find_element(By.XPATH,"//span[text()='Phone number, username, or email']").send_keys("Pranav")
#driver.find_element(By.XPATH,"//span[text()='Password']").send_keys("Pranav@123")
#driver.find_element(By.XPATH,"//div[text()='Log in']").click()
#time.sleep(3)


driver.get("https://www.facebook.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//label[text()='Email address or mobile number']").send_keys("Pranav")
#driver.find_element(By.XPATH,"//label[text()='Password']").send_keys("Pranav@123")

driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
driver.back()

driver.find_element(By.XPATH,"//button[text()='Log in']").click()
time.sleep(3)