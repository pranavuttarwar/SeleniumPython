import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "//button[text()='Try it']").click()
time.sleep(3)
driver.switch_to.alert.send_keys("Pranav")
time.sleep(3)
driver.switch_to.alert.accept()
#driver.switch_to.default_content()
value=driver.find_element(By.XPATH, "//p[@id='demo']").text
print(value)
time.sleep(3)