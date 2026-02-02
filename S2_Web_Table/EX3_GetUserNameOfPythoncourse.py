import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("file:///C:/Users/Pranav%20Uttarwar/OneDrive/Desktop/table.html")
driver.maximize_window()
time.sleep(2)

#Get student name having course name python

StudentName=driver.find_element(By.XPATH,"//table[@id='studentTable']//td[text()='Python']//parent::tr/td[2]").text
print("Student Name who's course is python: ",StudentName)



#Additional case
multiple=driver.find_elements(By.XPATH,"//table[@id='studentTable']//td[text()='Python']//parent::tr/td[2]")

for i in multiple:
    print(i.text)


time.sleep(2)
driver.quit()