import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://www.websiteplanet.com/webtools/multiple-url/")
driver.maximize_window()
time.sleep(2)

#To find multiple element use find_elements

AllLinks=driver.find_elements(By.XPATH,"//a")

#Find number of available Links
print(len(AllLinks))

#get the name of the all link values

for linkname in AllLinks:
    print(linkname.text)

time.sleep(2)