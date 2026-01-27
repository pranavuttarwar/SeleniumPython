import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(5)

#Click on the New Tab btn
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()

#take the id of window/tab using window method.

AllIds=driver.window_handles

#Switch to child window -> change the selenium focus from main page to child page

driver.switch_to.window(AllIds[1])
time.sleep(2)
childwindtext=driver.find_element(By.XPATH,"//h1[@id='sampleHeading']").text
print("Childwindowtext: ",childwindtext)

time.sleep(2)

#change selenium focus from child page to main page
driver.switch_to.window(AllIds[0])
time.sleep(2)

#Click on the New window btn
driver.find_element(By.XPATH,"//button[text()='New Window']").click()

#Again take the id of all open window
allId2=driver.window_handles

driver.switch_to.window(allId2[2])
driver.maximize_window()
time.sleep(2)

#Again change selenium focus to main page.

driver.switch_to.window(AllIds[0])

#Click on the New Window Message

driver.find_element(By.XPATH,"//button[text()='New Window Message']").click()

#Take all tab/window ids
allId3=driver.window_handles
driver.switch_to.window(allId3[3])


