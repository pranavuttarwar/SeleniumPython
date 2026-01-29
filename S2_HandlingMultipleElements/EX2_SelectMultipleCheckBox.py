import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
driver.maximize_window()
time.sleep(2)

#Get All checkbox address
AllCheckboxAddress=driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']")

#Count the check box

print(len(AllCheckboxAddress))

for CheckboxAddress in AllCheckboxAddress:
    CheckboxAddress.click()
    time.sleep(1)

time.sleep(3)