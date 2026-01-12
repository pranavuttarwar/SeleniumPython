import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

#approch-1
#driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")



#approch2:
em=driver.find_element(By.XPATH,"//input[@name='email']")
em.send_keys("abc")


time.sleep(2)