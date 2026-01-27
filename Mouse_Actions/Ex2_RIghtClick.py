import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(2)

Loginhover=driver.find_element(By.XPATH,"//span[text()='Login']")
profile=driver.find_element(By.XPATH,"//a[@title='My Profile']")

action=ActionChains(driver)
action.move_to_element(Loginhover).perform()
time.sleep(2)
action.move_to_element(profile).perform()
time.sleep(2)
action.context_click().perform()

time.sleep(5)