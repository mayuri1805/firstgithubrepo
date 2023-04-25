from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("D:\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.globalsqa.com/demo-site/draganddrop")
driver.maximize_window()
driver.find_element(By.XPATH,"https://www.globalsqa.com/demoSite/practice/droppable/images/high_tatras_min.jpg")
actions=ActionChains(driver)



