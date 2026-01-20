#Example of Single frame
import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

iframeaddress=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")

driver.switch_to.frame(iframeaddress)

driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time.')]").click()

time.sleep(2)