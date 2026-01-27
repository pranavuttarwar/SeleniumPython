import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("287")
driver.find_element(By.XPATH,"//input[@name='submit']").click()
time.sleep(3)

#Click on dismiss
driver.switch_to.alert.dismiss()

time.sleep(3)

#again click on the submit button
driver.find_element(By.XPATH,"//input[@name='submit']").click()

#Get pop up text
popuptext=driver.switch_to.alert.text
print("Pop up text: ",popuptext)

time.sleep(3)

#Click on Ok or Yes
driver.switch_to.alert.accept()

time.sleep(3)

nextpopuptext=driver.switch_to.alert.text
print("Next popup text: ",nextpopuptext)

time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)

