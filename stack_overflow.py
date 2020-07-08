from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import os
driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

driver.get('https://stackoverflow.com/')

driver.maximize_window()

driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()

driver.find_element_by_xpath('//*[@id="email"]').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys('#######')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]').click()
driver.find_element_by_xpath('//*[@id="password"]').send_keys("#######")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="submit-button"]').click()
time.sleep(2)

driver.get('https://stackoverflow.com/users/11321166/gokul-nath')

print(driver.find_element_by_xpath('//*[@id="top-cards"]/aside[2]/div/div/div[2]/div[2]/div/div[1]/span').text)
time.sleep(5)

driver.close()








