import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)
#find element on the screen
instL=driver.find_element(By.XPATH, "//a[text()='Instagram']")

#Scroll till the element
act = ActionChains(driver)
act.scroll_to_element(instL).perform()
time.sleep(3)




