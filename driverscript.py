import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(executable_path="D:\chromedriver\chromedriver_win32/chromedriver.exe"))
driver.get("http://127.0.0.1:8000/login?next=/")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("user")
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("user")
driver.find_element(By.XPATH,'//button[@class="btn btn-sm rounded-0 btn-primary"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//ul[@class="navbar-nav me-auto mb-2 mb-lg-0"]//li[2]').click()
driver.find_element(By.XPATH,'//button[@id="add_new"]').click()
time.sleep(10)
# driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/a').click()
driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("Rutu Palandurkar")
driver.find_element(By.XPATH,'//input[@id="phoneno"]').send_keys(9881086537)
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="fromdate"]').click()
driver.find_element(By.XPATH,'//input[@name="todate"]').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td/button[2]').click()
driver.find_element(By.XPATH,'//button[@id="add_new"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("Rutu Palandurkar")
driver.find_element(By.XPATH,'//input[@id="phoneno"]').send_keys(9881086537)
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/button[2]').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[4]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="name"]').click()
driver.find_element(By.XPATH,'//input[@id="name"]').clear()
driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("mayuri khade")
driver.find_element(By.XPATH,'//input[@id="phoneno"]').click()
driver.find_element(By.XPATH,'//input[@id="phoneno"]').clear()
driver.find_element(By.XPATH,'//input[@id="phoneno"]').send_keys(9156460795)
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
driver.close()
