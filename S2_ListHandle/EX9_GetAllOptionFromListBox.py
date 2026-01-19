import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/r.php?entry_point=login")

#Step1:
month=driver.find_element(By.XPATH,"//select[@name='birthday_month']")

#Step2
s=Select(month)

s.select_by_value("3")

Alloptions=s.options

for option in Alloptions:
    print(option.text)

time.sleep(5)


FirstOption=s.first_selected_option
print(FirstOption.text)
time.sleep(5)