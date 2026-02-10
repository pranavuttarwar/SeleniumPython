import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

search=(driver.find_element(By.XPATH,"(//input[@name='q'])[1]"))
search.send_keys("Redmi 12G")
search.send_keys(Keys.ENTER)

Rating=driver.find_element(By.XPATH,"(//div[@class='jIjQ8S'])[1]//span[@class='PvbNMB']//span[1]/span[3]").text
time.sleep(2)
print("Rating of mobile is: ",Rating)

time.sleep(5)
