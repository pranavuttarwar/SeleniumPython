import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("287")
driver.find_element(By.XPATH,"//input[@name='submit']").click()
time.sleep(3)

alert=driver.switch_to.alert
Popuptext=alert.text
print(Popuptext)
time.sleep(3)
alert.dismiss()

driver.find_element(By.XPATH,"//input[@name='submit']").click()

alert.accept()
Nextpopuptext=alert.text
print(Nextpopuptext)
time.sleep(3)
alert.accept()
time.sleep(3)
