#Example of Nested frame
import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")

#Approch1: #By iframe ID or Name
driver.switch_to.frame("iframeResult")

#Approch2: # By frame web element
inner_frame=driver.find_element(By.XPATH,"//iframe[@title='W3Schools Free Online Web Tutorials']")
time.sleep(2)
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH,"//a[text()='HTML']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@onclick='open_menu()']").click()

time.sleep(5)