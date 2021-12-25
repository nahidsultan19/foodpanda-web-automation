from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

# this for which browser i want to user for
driver = webdriver.Chrome(PATH)

# for open the browser
driver.get('https://www.rokomari.com/book')
# print(driver.title)
# driver.close()
time.sleep(2)
link = driver.find_elements_by_class_name('user-menu')
link.click()
