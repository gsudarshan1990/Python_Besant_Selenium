import time

from selenium import webdriver

driver = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://ui.cogmento.com/')
driver.find_element_by_xpath('//input[@name = "email"]').send_keys('XXXXX')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('XXXXX')
driver.find_element_by_xpath("//div[text()='Login']").click()
driver.find_element_by_xpath("//a[@href='/contacts']//span[text()='Contacts']").click()
driver.find_element_by_xpath('(//button[@class="ui linkedin button"])[3]').click()
driver.find_element_by_name("first_name").send_keys('sudarshan')
driver.find_element_by_name("last_name").send_keys("Govinda")
driver.find_element_by_name("middle_name").send_keys("IT Engineer")
driver.find_element_by_xpath("//input[@placeholder ='Email address']").send_keys('XXXXX')
driver.find_element_by_xpath('//textarea[@name ="description"]').send_keys('This is the first example of selenium on CRM')
driver.find_element_by_xpath("//button[text()='Save']").click()
driver.find_element_by_xpath("//div[@class='ui buttons']//div").click()
driver.find_element_by_xpath("//a//span[text()='Log Out']").click()
driver.close()


