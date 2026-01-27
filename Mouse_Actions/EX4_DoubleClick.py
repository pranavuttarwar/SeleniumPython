import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)
#Double click element
button=driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
act=ActionChains(driver)
act.double_click(button).perform()

time.sleep(2)

driver.switch_to.alert.accept()
