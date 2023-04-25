import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

import time
driver=webdriver.Chrome(service=Service(executable_path="D:\chromedriver\chromedriver_win32/chromedriver.exe"))
driver.get("http://mitintech.com/admin/")
driver.maximize_window()
driver.find_element(By.NAME, 'username').send_keys('mayuri')
driver.find_element(By.NAME, 'password').send_keys('mayuri')
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
driver.find_element(By.XPATH,'//a[@href="/admin/master/tblbookseries/add/"]').click()
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# driver.find_element(By.XPATH,'//img[@src="/static/admin/img/icon-changelink.svg"]').click()
# driver.find_element(By.NAME,'name').clear()
# driver.find_element(By.NAME,'name').send_keys('English')
# time.sleep(10)
# driver.find_element(By.NAME,'description').click()

# Subject script
# driver.find_element(By.CLASS_NAME,'addlink').click()
driver.find_element(By.XPATH,'//a[@href="/admin/master/tblbookseries/add/"]').click()
driver.find_element(By.NAME,'name').send_keys('hfjgfkghk')
# driver.find_element(By.NAME,'description').send_keys('hdfhdhfj')
driver.find_element(By.NAME,'_save').click()

# Class script

driver.find_element(By.XPATH,'//a[@href="/admin/master/tblclass/add/"]').click()
driver.find_element(By.NAME,'name').send_keys('pre-nursury')
driver.find_element(By.XPATH,'//input[@value="Save"]').click()

# Book series

driver.find_element(By.XPATH,'//a[@href="/admin/master/tblbookseries/add/"]').click()
driver.find_element(By.NAME,'subject').click()
driver.find_element(By.CLASS_NAME,'vTextField').send_keys('matchbox house')
driver.find_element(By.NAME,'_save').click()

# Chapter

driver.find_element(By.XPATH,'//a[@href="/admin/master/tblchapter/add/"]').click()
driver.find_element(By.NAME,'name').send_keys('HTML')
driver.find_element(By.NAME,'subject').click()
driver.find_element(By.NAME,'bookseries').click()
driver.find_element(By.NAME,'classid').click()
driver.find_element(By.NAME,'_save').click()
