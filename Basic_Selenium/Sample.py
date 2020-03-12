import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("E:\Python_Besant_Selenium\drivers\chromedriver.exe")
driver.get("https://freecrm.co.in/")
driver.maximize_window()
login_element=driver.find_element_by_xpath("//span[text()='Log In']")
login_element.click()
email_element=driver.find_element_by_xpath("//input[@name='email']")
password_element=driver.find_element_by_xpath("//input[@name='password']")
email_element.send_keys("XXXXXX")
password_element.send_keys("XXXX")
crm_login_element=driver.find_element_by_xpath("//div[text()='Login']")
crm_login_element.click()
time.sleep(5)
contact_element=driver.find_element_by_xpath("//span[text()='Contacts']")
contact_element.click()
new_url_element=driver.find_element_by_xpath("//a[@href=\"/contacts/new\"]")
new_url_element.click()
time.sleep(5)
contact_firstname_element=driver.find_element_by_xpath("//input[@name='first_name']")
contact_firstname_element.send_keys("Sudar")
contact_lastname_element=driver.find_element_by_xpath("//input[@name='last_name']")
contact_lastname_element.send_keys("Govind")
contact_middle_name_element=driver.find_element_by_xpath("//input[@name='middle_name']")
contact_middle_name_element.send_keys("XXX")
contact_company_name=driver.find_element_by_xpath("//div[@name=\"company\"]//input[@type='text']")
contact_company_name.send_keys("M")
contact_company_name.send_keys(Keys.ENTER)

access_button=driver.find_element_by_xpath("//button[text()='Public']")
access_button.click()
time.sleep(2)
user_select_dropdown=driver.find_element_by_xpath("//div[text()='Select users allowed access']")
user_select_dropdown.click()
user_select_element=driver.find_element_by_xpath("//div[@class='twelve wide field']//div[@role=\"option\"]//span")
user_select_element.click()
tag_element=driver.find_element_by_xpath("//label[@for=\"tags\"]//div//input[@type='text']")
tag_element.send_keys("Python")
tag_element.send_keys(Keys.ENTER)
email_address_element=driver.find_element_by_xpath("//input[@placeholder='Email address']")
email_address_element.send_keys("sudarshan.suraj@yahoo.com")
personal_email_element=driver.find_element_by_xpath("//input[contains(@placeholder,'Personal email')]")
personal_email_element.send_keys("sudarshan_google@gmail.com")
description_element=driver.find_element_by_xpath("//textarea[@name='description']")
description_element.send_keys("This is used for sample automation testing")
channel_type=driver.find_element_by_xpath("//div[@name=\"channel_type\"]")
channel_type.click()
channel_options=driver.find_elements_by_xpath("//div[@name=\"channel_type\"]//div[@role='option']")

for channel in channel_options:
    if channel.text == 'Facebook':
        channel_text = channel.text
        print(channel_text)
        channel.click()
        break

link_profile_element=driver.find_element_by_xpath("//div[@role=\"option\"]//span[text()='"+channel_text+"']/../../../following-sibling::div//input")
link_profile_element.send_keys("www."+channel_text+".com")
time_zone_element=driver.find_element_by_xpath("//div[@name=\"timezone\"]")
time_zone_element.click()
time_zone_countries=driver.find_elements_by_xpath("//div[@name=\"timezone\"]//div[@role='listbox']//div")
time_zone_countries[4].click()
address_element=driver.find_element_by_name("address")
address_element.send_keys("Perung")
city_element=driver.find_element_by_name("city")
city_element.send_keys("Ch")
state_element=driver.find_element_by_name("state")
state_element.send_keys("TN")
zip_element=driver.find_element_by_name("zip")
zip_element.send_keys("500060")
drop_down_country=driver.find_element_by_xpath("//div[@name='country']")
drop_down_country.click()
country_list=driver.find_elements_by_xpath("//div[@name=\"country\"]//div[@role=\"listbox\"]//div")
for country in country_list:
    if country.text == 'India':
        country.click()
        break
phone_country_element=driver.find_element_by_name("hint")
phone_country_element.click()
phone_country_list=driver.find_elements_by_xpath("//div[@name=\"hint\"]//div[@role=\"listbox\"]//div")
for phone_country in phone_country_list:
    if phone_country.text == 'India':
        phone_country.click()
        break

phone_isd_code=driver.find_element_by_xpath("//input[@placeholder=\"Number\"]")
phone_isd_code.send_keys("91")
phone_number=driver.find_element_by_xpath("//input[@placeholder=\"Home, Work, Mobile...\"]")
phone_number.send_keys("97383602377")
position_element=driver.find_element_by_name("position")
position_element.send_keys("IT Analyst")
department_element=driver.find_element_by_name("department")
department_element.send_keys("Banking Domain")
supervisor_element=driver.find_element_by_xpath("//div[@name='supervisor']//input[@type='text']")
supervisor_element.send_keys("Ram Charan Teja")
supervisor_element.send_keys(Keys.ENTER)
assitant_element=driver.find_element_by_xpath("//div[@name='assistant']//input[@type='text']")
assitant_element.send_keys("Swaminathan")
assitant_element.send_keys(Keys.ENTER)
referred_by=driver.find_element_by_xpath("//div[@name='referred_by']//input[@type='text']")
referred_by.send_keys("Rakesh")
referred_by.send_keys(Keys.ENTER)
status_list=driver.find_elements_by_xpath("//div[@name='status']//div")
status_element=driver.find_element_by_name("status")
state_element.click()
for status in status_list:
    if status.text == 'Active':
        status.click()
        break
source_element=driver.find_element_by_name("source")
source_element.click()
source_list=driver.find_elements_by_xpath("//div[@name='source']//div")
for source in source_list:
    if source.text == 'Referral':
        source.click()
        break
category_element=driver.find_element_by_name("category")
category_element.click()
category_list=driver.find_elements_by_xpath("//div[@name='category']//div")
for category in category_list:
    if category.text == 'Affiliate':
        category.click()
        break
do_not_call_element=driver.find_element_by_name("do_not_call")
driver.execute_script("arguments[0].click();",do_not_call_element)
do_not_text_element=driver.find_element_by_name("do_not_text")
driver.execute_script("arguments[0].click();",do_not_text_element)
do_not_email_element=driver.find_element_by_name("do_not_email")
driver.execute_script("arguments[0].click();",do_not_email_element)
birth_day_element=driver.find_element_by_name("day")
birth_day_element.send_keys("5")
month_element=driver.find_element_by_name("month")
month_element.click()
month_element_list=driver.find_elements_by_xpath("//div[@name='month']//div")
for month in month_element_list:
    if month.text == 'April':
        month.click()
        break
year_element=driver.find_element_by_name("year")
year_element.send_keys("2020")
Identifier_element=driver.find_element_by_name("identifier")
Identifier_element.send_keys("Good Identifer")

save_element=driver.find_element_by_xpath("//i[@class='save icon']")
save_element.click()