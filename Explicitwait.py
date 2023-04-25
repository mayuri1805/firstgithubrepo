from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from service import Service

driver=webdriver.Chrome(service=Service(executable_path="D:\chromedriver\chromedriver_win32/chromedriver.exe"))

driver.get("https://automationtesting.in")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
switchto=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"SwitchTo")))
# driver.find_element(By.PARTIAL_LINK_TEXT,"SwitchTo")
actions=ActionChains(driver)
actions.move_to_element(switchto)
actions.perform()
driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts").click()
