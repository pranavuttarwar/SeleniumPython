import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/table.html")
driver.maximize_window()
time.sleep(2)

#get total number of columns in the row

value=driver.find_element(By.XPATH,"//table[@id='studentTable']//tr[5]/td[2]").text
print("Specific index value: ",value)

print("Print All Students Name")
allNames=value=driver.find_elements(By.XPATH,"//table[@id='studentTable']//tr/td[2]")
for i in allNames:
    print("All Student Names: ", i.text)

time.sleep(2)
driver.quit()