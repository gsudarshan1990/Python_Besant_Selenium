from selenium import webdriver
import time

driver = webdriver.Chrome("E:\Python_Besant_Selenium\drivers\chromedriver.exe")
driver.get("https://www.edx.org/")
driver.maximize_window()
signin_element=driver.find_element_by_xpath("(//a[text()='Sign In'])[2]")
signin_element.click()
time.sleep(10)
#driver.switch_to.frame(driver.find_element_by_xpath("//form[@name=\"login\"]"))
email_element=driver.find_element_by_xpath("//input[@id='login-email']")
email_element.send_keys("sudarshan.*****@yahoo.com")
password_element=driver.find_element_by_xpath("//input[@id='login-password']")
password_element.send_keys("********")
login_button=driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()


