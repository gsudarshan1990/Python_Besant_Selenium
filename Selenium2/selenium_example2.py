from selenium import webdriver

driver = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('http://demo.guru99.com/test/newtours/register.php')
driver.find_element_by_name("firstName").send_keys('sonu')
driver.find_element_by_name('lastName').send_keys("garimella")
driver.find_element_by_xpath("//input[@name='phone']").send_keys("84452443254")
driver.find_element_by_id("userName").send_keys("sonu90@gmail.com")
driver.find_element_by_name("address1").send_keys('chaitanyapuri')
driver.find_element_by_xpath("//input[@name='city']").send_keys('Hyderabad')
driver.find_element_by_xpath("//input[@name='state']").send_keys("Telengana")
driver.find_element_by_name('postalCode').send_keys('500060')
driver.find_element_by_xpath("//input[@id='email']").send_keys('sonu90@gmail.com')
driver.find_element_by_xpath("//input[@name='password']").send_keys('hacker1223')
driver.find_element_by_name('confirmPassword').send_keys('hacker1223')
driver.find_element_by_name("submit").click()

