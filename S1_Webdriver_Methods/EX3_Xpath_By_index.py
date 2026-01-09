import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/reg/?entry_point=login&next=")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Pranav")
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("Uttarwar")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("123456789")
#driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
#driver.back()

#driver.find_element(By.XPATH,"//button[text()='Log in']").click()
time.sleep(3)