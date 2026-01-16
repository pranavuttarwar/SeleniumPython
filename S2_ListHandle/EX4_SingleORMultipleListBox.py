import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")

result=driver.find_element(By.XPATH,"//select[@name='birthday_day']")

s=Select(result)

val=s.is_multiple
print("List Multiselect for facebook page",val)

time.sleep(1)

driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/Multiselect%20HTML.html")

s1=Select(result)

val1=s1.is_multiple
print("List Multiselect for My html page",val1)