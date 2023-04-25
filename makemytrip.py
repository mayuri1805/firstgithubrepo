import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
driver=webdriver.Chrome(service=Service(executable_path="D:\chromedriver\chromedriver_win32/chromedriver.exe"))
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Flights').click()
driver.find_element(By.XPATH, '//li[@data-cy="roundTrip"]/span').click()
driver.find_element(By.ID, 'fromCity').click()
time.sleep(3)
driver.find_element(By.XPATH, '//input[@placeholder="From"]').send_keys('Nagpur')
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'calc60').click()
time.sleep(3)
driver.find_element(By.ID, 'toCity').click()
time.sleep(3)
driver.find_element(By.XPATH, '//input[@placeholder="To"]').send_keys('Pune')
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'calc60').click()
time.sleep(3)

driver.find_element(By.XPATH, '//div[@aria-label="Thu Apr 13 2023"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//div[@aria-label="Thu Apr 20 2023"]').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'SEARCH').click()
time.sleep(20)

name = driver.find_element(By.XPATH, '//span[@class="boldFont blackText"]')
fair = driver.find_element(By.XPATH, '//p[@class="blackText fontSize16 blackFont"]')
