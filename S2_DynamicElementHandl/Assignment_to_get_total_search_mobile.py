import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

search=(driver.find_element(By.XPATH,"(//input[@name='q'])[1]"))
search.send_keys("Redmi 12G")
search.send_keys(Keys.ENTER)

#get all searched mobiles
AllMobName=driver.find_elements(By.XPATH,"//div[@class='jIjQ8S']//div[@class='RG5Slk']")
print("Total Mobile Result: ",len(AllMobName))
for name in AllMobName:
    print(name.text)

#Get all mobile price
print("-------------------------------")
PriceofMobile=driver.find_elements(By.XPATH,"//div[@class='col col-5-12 mao5dl']//div[@class='oFEPlD']//div[@class='hZ3P6w DeU9vF']")
print("Search mobile price: ",len(PriceofMobile))

for price in PriceofMobile:
    print(price.text)
    time.sleep(1)


time.sleep(10)
