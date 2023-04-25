from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("9881085407")
driver.find_element(By.ID,"pass").send_keys("abcde")
driver.find_element(By.NAME,"login").click()
driver.find_element(By.LINK_TEXT,"Forgotten password?").click()


