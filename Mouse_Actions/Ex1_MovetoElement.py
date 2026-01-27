import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(2)

Loginhover=driver.find_element(By.XPATH,"//span[text()='Login']")

action=ActionChains(driver)
action.move_to_element(Loginhover).perform()
time.sleep(3)