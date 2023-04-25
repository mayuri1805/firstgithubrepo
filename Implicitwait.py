from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://automationtesting.in")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()