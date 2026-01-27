import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.mobikwik.com/")

driver.maximize_window() #Used to maximize the browser

driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()

time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='userId']").send_keys("0999999999")

time.sleep(5)