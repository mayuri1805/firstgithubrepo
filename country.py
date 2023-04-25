import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome("D:\chromedriver\chromedriver_win32.exe")
driver.get("https://automationtesting.in")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
time.sleep(3)
selectcountry=Select(driver.find_element(By.ID,"country"))
time.sleep(6)
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span').click()
driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("India")
driver.find_element(By.XPATH,'//*[@id="select2-country-results"]/li[1]').click()
driver.find_element(By.ID,"msdd").click()
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a').click()
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/label').click()