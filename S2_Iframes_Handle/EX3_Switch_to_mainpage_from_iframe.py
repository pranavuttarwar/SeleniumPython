#Example of Single frame
import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
#Approch1:
iframeaddress=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")

driver.switch_to.frame(iframeaddress)

driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time.')]").click()

#Switch from iframe to main page
#Approch1
#driver.switch_to.default_content()

#Approch2
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()
time.sleep(2)