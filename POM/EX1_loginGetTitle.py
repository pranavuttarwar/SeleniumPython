import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

#Enter username
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")

#Enter Password:
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")

#Click on the login
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

time.sleep(1)

#get title
Actualtitle=driver.find_element(By.XPATH,"//div[@class='app_logo']").text

ExpectedTitle="Swag Labs"
if Actualtitle == ExpectedTitle:
    print("Success Title Match")
else:
    print("Failed Title not Match")
