import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()
time.sleep(2)
#find source and destination element

src=driver.find_element(By.XPATH,"//img[@src='logo.png']")
dest=driver.find_element(By.XPATH,"//div[@id='droparea']")

act=ActionChains(driver)
act.scroll_by_amount(0,100).perform()
time.sleep(2)
#act.drag_and_drop(src,dest).perform()
act.click_and_hold(src).move_to_element(dest).release().perform()

time.sleep(5)


