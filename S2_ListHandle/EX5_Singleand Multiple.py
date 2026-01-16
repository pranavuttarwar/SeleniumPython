import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/Multiselect%20HTML.html")
result=driver.find_element(By.XPATH,"//select[@id='courseList']")
s1=Select(result)

val1=s1.is_multiple
print("List Multiselect for My html page:",val1)