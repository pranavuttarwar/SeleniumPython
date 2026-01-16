import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/r.php?entry_point=login")

#Step1:
day=driver.find_element(By.XPATH,"//select[@name='birthday_day']")

#Step2
s=Select(day)

#Step3

#Option1
s.select_by_visible_text("17")

#option2

month=driver.find_element(By.XPATH,"//select[@name='birthday_month']")
s1=Select(month)
s1.select_by_index(2)

#option3

year=driver.find_element(By.XPATH,"//select[@name='birthday_year']")
s2=Select(year)
s2.select_by_value("1997")
time.sleep(2)