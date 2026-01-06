import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")

driver.maximize_window() #Used to maximize the browser
time.sleep(5)

driver.fullscreen_window() #it used to to the full screen
time.sleep(5)

driver.minimize_window()
driver.maximize_window()
time.sleep(5)

actualtitle=driver.title #attribute/return type used to get the web page title
print("1st Title of the web page:",actualtitle)
print("Title get 2nd approch:",driver.title)

print("Current URL:",driver.current_url) #To get the URL in the

driver.get("https://www.google.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
driver.refresh()
time.sleep(5)

driver.minimize_window() #Used to minimize the browser
time.sleep(5)


driver.close()  #To close the current tab.
driver.quit() #To close the browser.