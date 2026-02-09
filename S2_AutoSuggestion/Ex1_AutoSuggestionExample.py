import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

Exptext="iphone 16"
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("iphone")
time.sleep(2)
ListofItem=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]/li//div[@class='wM6W7d']")

for item in ListofItem:
    #print(item.text)
    actultxt=item.text
    if actultxt==Exptext:
        item.click()
        break


time.sleep(20)
driver.quit()