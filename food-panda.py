from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'

# this for which browser i want to user for
driver = webdriver.Chrome(PATH)

# test case 001
driver.get('https://www.google.com/')

driver.maximize_window()
# url = 'https://www.foodpanda.com.bd/'
search_box = driver.find_element_by_name('q')
time.sleep(5)

search_box.send_keys('https://www.foodpanda.com.bd')
time.sleep(1)

search_box.send_keys(Keys.ENTER)
enter_link = driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')

enter_link.click()

time.sleep(2)
# complete home page section

# start login
driver.find_element_by_class_name('login-label').click()
# check_box = driver.find_element_by_class_name(
#     'recaptcha-checkbox-border')
# check_box.submit()
