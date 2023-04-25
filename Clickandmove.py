import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\seleniumdriver\chromedriver_win32.zip\chromedriver.exe")

driver.get("https://automationtesting.in")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
actions=ActionChains(driver)
switchto=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"SwitchTo")))
actions.move_to_element(switchto).perform()
windlink=driver.find_element(By.PARTIAL_LINK_TEXT,"Windows")
actions.click_and_hold(windlink).perform()
time.sleep(10)
actions.release(on_element=windlink).perform()

