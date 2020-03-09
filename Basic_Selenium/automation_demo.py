from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome("E:\SeleniumPrgms\drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
first_name_element=driver.find_element_by_xpath("//input[@placeholder=\"First Name\"]")
first_name_element.send_keys("Sudarshan")
last_name_element=driver.find_element_by_xpath("//input[@placeholder=\"Last Name\"]")
last_name_element.send_keys("Suraj")
address_element=driver.find_element_by_xpath("//textarea[@ng-model=\"Adress\"]")
address_element.send_keys("Chennai")
email_element=driver.find_element_by_xpath("//input[@type=\"email\"]")
email_element.send_keys("patma.sridharan@gmail.com")
phone_element=driver.find_element_by_xpath("//input[@type=\"tel\"]")
phone_element.send_keys("9378153277")
radio_elements=driver.find_elements_by_xpath("//input[@type=\"radio\"]")
radio_elements[0].click()
check_box_element=driver.find_elements_by_xpath("//input[@type=\"checkbox\"]")
check_box_element[0].click()
language_element=driver.find_element_by_xpath("//div[@id=\"msdd\"]")
language_element.click()
languages_element=driver.find_elements_by_xpath("//li[@class='ng-scope']")
for language in languages_element:
    if language.text == 'Filipino':
        language.click()
select_skill = Select(driver.find_element_by_id('Skills'))
select_skill.select_by_index(4)
select_country = Select(driver.find_element_by_id('countries'))
select_country.select_by_index(10)
country_combo_box=driver.find_element_by_xpath("//span[@role=\"combobox\"]")
country_combo_box.click()
select_year = Select(driver.find_element_by_id('yearbox'))
select_year.select_by_index(67)
select_month=Select(driver.find_element_by_xpath("//select[@placeholder=\"Month\"]"))
select_month.select_by_index(7)
select_day=Select(driver.find_element_by_id("daybox"))
select_day.select_by_index(15)
first_password_element=driver.find_element_by_xpath("//input[@id=\"firstpassword\"]")
first_password_element.send_keys("Python_demo1")
confirm_password_element=driver.find_element_by_xpath("//input[@id=\"secondpassword\"]")
confirm_password_element.send_keys("Python_demo1")
submit_button=driver.find_element_by_id("submitbtn")
submit_button.click()



