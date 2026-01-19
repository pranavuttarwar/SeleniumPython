import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/Multiselect%20HTML.html")
result=driver.find_element(By.XPATH,"//select[@id='courseList']")
s1=Select(result)

s1.select_by_index(1)
s1.select_by_index(3)
s1.select_by_index(4)

selectedoption=s1.all_selected_options

for option in selectedoption:
    print(option.text)

time.sleep(5)