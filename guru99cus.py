import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path="D:\chromedriver\chromedriver_win32/chromedriver.exe")
# driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://demo.guru99.com/v4/index.php")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@name="uid"]').send_keys("mngr485684")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("nuzYmah")
driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()
driver.find_element(By.XPATH,'//a[@href="addcustomerpage.php"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="name"]').send_keys("Mayuri Khade")
# driver.find_element(By.XPATH,'//input[@name="rad2"]').send_keys("female")
driver.find_element(By.XPATH,'//input[@value="f"]').click()
driver.find_element(By.XPATH,'//*[@name="addr"]').send_keys(" Pawansut Nagar Ramna Maroti R33oad Nagpur")
driver.find_element(By.XPATH,'//*[@name="city"]').send_keys("Nagpur")
driver.find_element(By.XPATH,'//*[@name="state"]').send_keys("Maharastra")
driver.find_element(By.XPATH,'//input[@name="pinno"]').send_keys("440004")
driver.find_element(By.XPATH,'//input[@name="telephoneno"]').send_keys("9156460795")
driver.find_element(By.XPATH,'//input[@name="emailid"]').send_keys("mayurikhade1@gmail.com")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("mayuri18")
driver.find_element(By.XPATH,'//input[@id="dob"]').send_keys("18-05-1996")
driver.find_element(By.XPATH,'//input[@value="Submit"]').click()
alert=Alert(driver).accept()
# alert=Alert(driver).accept()
driver.find_element(By.XPATH,'//a[@href="EditCustomer.php"]').click()
driver.find_element(By.XPATH,'//input[@name="cusid"]').send_keys(68767)
driver.find_element(By.XPATH,'//input[@name="AccSubmit"]').click()
driver.find_element(By.XPATH,'//input[@name="sub"]').click()
alert=Alert(driver).accept()
driver.find_element(By.XPATH,'//a[@href="DeleteCustomerInput.php"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="cusid"]').send_keys(68767)
driver.find_element(By.XPATH,'//input[@name="AccSubmit"]').click()
alert=Alert(driver).dismiss()

