import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(2)

Loginhover=driver.find_element(By.XPATH,"//span[text()='Login']")
order=driver.find_element(By.XPATH,"//a[@title='Orders']")

action=ActionChains(driver)
action.move_to_element(Loginhover).perform()
time.sleep(2)
action.move_to_element(order).perform()
time.sleep(2)
action.click().perform()

time.sleep(5)