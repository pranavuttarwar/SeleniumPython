import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/Multiselect%20HTML.html")

#Step1:
result=driver.find_element(By.XPATH,"//select[@id='courseList']")

#step2

s=Select(result)

#step3

s.select_by_visible_text("Manual Testing")
s.select_by_value("automation")
s.select_by_index(3)
time.sleep(2)
s.deselect_by_index(1)
s.deselect_all()

time.sleep(5)