#Example of Single frame
import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")

driver.switch_to.frame("iframeResult")

textvalue=driver.find_element(By.XPATH,"//p[text()='An iframe with default borders:']").text
print(textvalue)

innerframe=driver.find_element(By.XPATH,"//iframe[@src='/default.asp'][1]")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH, "//a[@onclick='open_menu()']").click()

time.sleep(2)