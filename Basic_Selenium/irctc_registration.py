from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome("E:\Python_Besant_Selenium\drivers\chromedriver.exe")
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
username_element=driver.find_element_by_xpath("//input[@placeholder=\"User Name\"]")
username_element.send_keys("sudar19")
password_element=driver.find_element_by_xpath("//input[@name=\"usrPwd\"]")
password_element.send_keys("Sudar1990")
confirm_password_element=driver.find_element_by_xpath("//input[@name=\"cnfUsrPwd\"]")
confirm_password_element.send_keys("Sudar1990")
security_question_element=driver.find_element_by_xpath("//label[contains(text(),'Select Security')]")
security_question_element.click()

security_question_list=driver.find_elements_by_xpath("//div[@class='ui-dropdown-items-wrapper']//li")
for question in security_question_list:
    if question.text == 'What is your favorite past-time?':
        question.click()
        break

security_answer_element=driver.find_element_by_xpath("//input[@placeholder='Security Answer']")
security_answer_element.send_keys("Music")
preferred_language=driver.find_element_by_xpath("//label[contains(text(),'Select Preferred Language')]")
preferred_language.click()
language_list=driver.find_elements_by_xpath("(//div[@class='ui-dropdown-items-wrapper'])[2]//ul//li//span")
language_list[1].click()
firstname_element=driver.find_element_by_name("firstName")
firstname_element.send_keys("Sudarsha")
middlename_element=driver.find_element_by_name("middleName")
middlename_element.send_keys("XXXXX")
lastname_element=driver.find_element_by_name("lastname")
lastname_element.send_keys("Govinda")
gender_element_list=driver.find_elements_by_xpath("//input[@formcontrolname='gender']")
gender_element_list[0].click()
date_of_birth_text=driver.find_element_by_xpath("//p-calendar//span//input")
date_of_birth_text.click()
select_month=Select(driver.find_element_by_xpath("//select[contains(@class,'ui-datepicker-month')]"))
select_month.select_by_index(6)
select_year=Select(driver.find_element_by_xpath("//select[contains(@class,'ui-datepicker-year')]"))
select_year.select_by_index(20)
date_widget_form=driver.find_element_by_xpath("//table[contains(@class,'ui-datepicker-calendar')]//tbody")
dates=date_widget_form.find_elements_by_tag_name("td")
for date in dates:
    if date.text == '20':
        date.click()
        break
occupation_element=driver.find_element_by_xpath("//label[text()='Select Occupation']")
occupation_element.click()
occupation_list=driver.find_elements_by_xpath("(//div//div[@class='ui-dropdown-items-wrapper'])[3]//ul//li")
for occupation in occupation_list:
    if occupation.text =='PRIVATE':
        occupation.click()
        break
marital_status_element=driver.find_elements_by_xpath("//input[@formcontrolname='martitalS']")
marital_status_element[1].click()
select_country=Select(driver.find_element_by_xpath("//select[@formcontrolname=\"resCountry\"]"))
select_country.select_by_visible_text("India")

email_element=driver.find_element_by_id("email")
email_element.send_keys("sudarshan_google@gmail.com")
#isd_element=driver.find_element_by_id("isd")
#isd_element.send_keys("91")
mobile_element=driver.find_element_by_id("mobile")
mobile_element.send_keys("9378153277")
select_nationality=Select(driver.find_element_by_xpath("//select[@formcontrolname=\"nationality\"]"))
select_nationality.select_by_visible_text("India")
flat_element=driver.find_element_by_id("resAddress1")
flat_element.send_keys("100")
street_element=driver.find_element_by_id("resAddress2")
street_element.send_keys("some street")
area_element=driver.find_element_by_id("resAddress3")
area_element.send_keys("Some Area")
pincode_element=driver.find_element_by_name("resPinCode")
pincode_element.send_keys('600063')
state_element=driver.find_element_by_id("resState")
state_element.send_keys("Tamil Nadu")
select_city=Select(driver.find_element_by_xpath("//select[@formcontrolname=\"resCity\"]"))
select_city.select_by_index(1)
select_postoffice=Select(driver.find_element_by_xpath("//select[@formcontrolname=\"resPostOff\"]"))
select_postoffice.select_by_index(1)
phone_element=driver.find_element_by_id("resPhone")
phone_element.send_keys("9186730833")
copy_residence_list=driver.find_elements_by_xpath("//input[@formcontrolname='officeSameAsRes']")
copy_residence_list[0].click()
term_condition_element=driver.find_element_by_xpath("//input[@formcontrolname=\"termCondition\"]")
webdriver.ActionChains(driver).move_to_element(term_condition_element ).click(term_condition_element ).perform()
button_element=driver.find_element_by_xpath("//button//b[text()='REGISTER']")
button_element.click()