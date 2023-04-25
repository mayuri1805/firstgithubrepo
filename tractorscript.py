import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(executable_path="C:\\chromedriver.exe"))
# (executable_path="C:\\chromedriver.exe")
driver.get("http://127.0.0.1:8000/login?next=/")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("user")
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("user")
driver.find_element(By.XPATH,'//button[@class="btn btn-sm rounded-0 btn-primary"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//a[@href="/tractor"]').click()
driver.find_element(By.XPATH,'//button[@id="add_new"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="tractorno"]').send_keys("MH-40-NG-8496")
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//button[@id="add_new"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@id="tractorno"]').send_keys("MH-41-NG-8004")
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[4]/a').click()
time.sleep(6)
driver.find_element(By.XPATH,'//button[@id="confirm"]').click()
time.sleep(5)
# driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[5]/a/button').click()
driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[3]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="tractorno"]').click()
driver.find_element(By.XPATH,'//input[@name="tractorno"]').clear()
driver.find_element(By.XPATH,'//input[@name="tractorno"]').send_keys("MH-40-NG-8745")
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="tractor-list"]/tbody/tr[2]/td[6]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="fromdate"]').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td/button[2]').click()
driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[5]/a/button').click()