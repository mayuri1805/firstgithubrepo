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
time.sleep(3)
driver.find_element(By.XPATH,'//a[@href="/tractor"]').click()
driver.find_element(By.CSS_SELECTOR)
# tag name are the input, spam, a,and etc...it is suggestable to use tag name..because there will be many tag name...
# so it is not suggestable to use tag name ....if it is unique then you can use