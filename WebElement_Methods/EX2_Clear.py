import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
#approch-1
#driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")
#driver.find_element(By.XPATH,"//input[@name='email']").clear()
#driver.find_element(By.XPATH,"//input[@name='email']").send_keys("XYZ")


#approch2:
em=driver.find_element(By.XPATH,"//input[@name='email']")
em.send_keys("abc")
time.sleep(1)
em.clear()

em.send_keys("XYZ")
time.sleep(2)

time.sleep(2)