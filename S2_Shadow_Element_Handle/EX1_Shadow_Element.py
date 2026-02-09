import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://selectorshub.com/xpath-practice-page/")

shadow=driver.find_element(By.XPATH,"//h6[text()='Shadow DOM']")
act = ActionChains(driver)
act.scroll_to_element(shadow).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='userName']").shadow_root.find_element(By.CSS_SELECTOR,"#kils").send_keys("HI")
time.sleep(12)
