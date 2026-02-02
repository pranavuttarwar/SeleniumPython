import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/table.html")
driver.maximize_window()
time.sleep(2)

#get total number of columns in the row

totalRows=driver.find_elements(By.XPATH,"//table[@id='studentTable']//tr[2]/td")
print("Total Columns in the table: ",len(totalRows))
time.sleep(2)
driver.quit()