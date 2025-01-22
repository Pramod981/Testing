#Impactguru Testing Site
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.impactguru.com/")
driver.maximize_window()
time.sleep(10)

driver.find_element(By.XPATH,"//a[text()='Start a free Fundraiser']").click()
time.sleep(8)
driver.back()
time.sleep(5)


# driver.find_element(By.ID,"//a[@id='dropdown02']").click()
# time.sleep(4)
# driver.find_element(By.XPATH,"//a[@class='dropdown-item currency-change'][2]").click()
# time.sleep(5)
