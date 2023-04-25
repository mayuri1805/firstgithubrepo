import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://automationtesting.in")
driver.maximize_window()
# driver.close()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
time.sleep(5)
switchto=driver.find_element(By.PARTIAL_LINK_TEXT,"SwitchTo")

actions=ActionChains(driver)
actions.perform()
# actions.click(driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts").click()










