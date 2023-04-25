import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://automationtesting.in")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
time.sleep(7)
select=Select(driver.find_element(By.XPATH,'//select[@id="Skills"]'))
select.select_by_visible_text('C++')
driver.find_element(By.ID,'firstpassword').send_keys("mkhade")
driver.find_element(By.XPATH,'//input[@id="secondpassword"]').send_keys("mkhade")
# driver.find_element(By.XPATH,'//*[@id="yearbox"]').click()
# driver.find_element(By.XPATH,'//*[@id="yearbox"]/option[79]').click()
selyear=Select(driver.find_element(By.XPATH,'//select[@id="yearbox"]'))
selyear.select_by_index(81)
selmon=Select(driver.find_element(By.XPATH,'//select[@placeholder="Month"]'))
selmon.select_by_index(5)
seldate=Select(driver.find_element(By.XPATH,'//select[@id="daybox"]'))
seldate.select_by_index(18)

# driver.find_element(By.PARTIAL_LINK_TEXT,"Submit").click()
actions=ActionChains(driver)
driver.find_element(By.PARTIAL_LINK_TEXT,'SwitchTo').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Alert').click()
driver.find_element(By.XPATH,'//button[@onclick="alertbox()"]').click()
alert=Alert(driver).accept()
driver.find_element(By.XPATH,'//a[@href="#CancelTab"]').click()
driver.find_element(By.XPATH,'//button[@onclick="confirmbox()"]').click()
alert=Alert(driver).accept()
driver.find_element(By.XPATH,'//a[@href="#Textbox"]').click()
driver.find_element(By.XPATH,'//button[@onclick="promptbox()"]').click()
alert=Alert(driver).accept()
driver.find_element(By.PARTIAL_LINK_TEXT,'SwitchTo').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Frames').click()
driver.find_element(By.XPATH,'//a[@href="#Multiple"]').click()

driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]'))
