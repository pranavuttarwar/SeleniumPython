import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com")
time.sleep(2)
logo=driver.find_element(By.XPATH, "//img[@class='fb_logo _8ilh img']")
logo.screenshot("D:/Python Notes/Screenshots//demo1.png")