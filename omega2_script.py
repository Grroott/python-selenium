from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

driver.get('https://www.libertymutual.com/get-a-quote')

driver.maximize_window()

driver.find_element_by_xpath(
    '//*[@id="1555468516747"]/section/div[2]/section/form/div[1]/div[3]/div/div[1]').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="zipcode-1555468516747-1555468516747"]').click()

driver.find_element_by_xpath('//*[@id="zipcode-1555468516747-1555468516747"]').send_keys('03878')

time.sleep(1)

driver.find_element_by_xpath(
    '//*[@id="1555468516747"]/section/div[2]/section/form/div[2]/div[5]/div/div/button').submit()

driver.implicitly_wait(10)
try:
    time.sleep(10)
    ok =  driver.find_element_by_xpath('//*[@id="discount-marketing-modal"]/footer/button')
    ActionChains(driver).move_to_element(ok).pause(1).click(ok).perform()
    
except:
    
    pass

driver.implicitly_wait(25)

driver.find_element_by_xpath('//*[@id="first-name-input"]').click()

driver.find_element_by_xpath('//*[@id="first-name-input"]').send_keys('Xxtestxx')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="last-name-input"]').click()

driver.find_element_by_xpath('//*[@id="last-name-input"]').send_keys('Xxtestxx')

time.sleep(2)

driver.find_element_by_xpath('//*[@id="birth-date-input"]').click()

driver.find_element_by_xpath('//*[@id="birth-date-input"]').send_keys('01/07/1996')

time.sleep(2)

driver.find_element_by_xpath('//*[@id="about-you-next"]').submit()

time.sleep(10)
try:

    Select(driver.find_element_by_xpath('//*[@id="vehicle-year-select-select"]')).select_by_visible_text('2010')

    driver.implicitly_wait(2)
except:

    pass

time.sleep(3)

driver.find_element_by_xpath('//*[@id="top-makes"]/fieldset/div/div/div[3]/label/span[1]/span').click()


driver.implicitly_wait(2)

Select(driver.find_element_by_xpath('//*[@id="model-select"]')).select_by_visible_text('ACCORD')

time.sleep(1)

Select(driver.find_element_by_xpath('//*[@id="trim-select"]')).select_by_visible_text('CROSSTOUR')

driver.implicitly_wait(2)

Select(driver.find_element_by_xpath('//*[@id="bodyStyle-select"]')).select_by_visible_text('Utility - Two Wheel Drive 4 Door')

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="form-submit"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="app"]/main/div/div/form/div/div/div/div/div[1]')
driver.find_element_by_xpath('//*[@id="form-submit"]').click()
time.sleep(5)

Select(driver.find_element_by_xpath('//*[@id="purchaseYear-select"]')).select_by_visible_text('2010')

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="ownershipType"]/fieldset/div/label[1]/span/span[1]').click()

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="form-submit"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="next-cta"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="form-submit"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="maritalStatus"]/fieldset/div/label[2]/span').click()

driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="gender"]/fieldset/div/label[1]/span').click()

driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="drivers-submit-button"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="isGoodStudent"]/fieldset/div/label[1]/span').click()

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="phoneNumber-input"]').click()
driver.find_element_by_xpath('//*[@id="phoneNumber-input"]').clear()
driver.find_element_by_xpath('//*[@id="phoneNumber-input"]').send_keys('9898989898')

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="drivers-submit-button"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="driver-recap-next"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="highestEducationLevel"]/fieldset/div/label[4]/span').click()

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="residenceType"]/fieldset/div/label[1]/span').click()

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="discounts-submit-button"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="right-track-tag-radio"]/fieldset/div/label[1]/span').click()

driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="discounts-next"]').click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="auto-policy-indicator"]/fieldset/div/label[2]/span').click()

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="auto-policy-indicator"]/fieldset/div/label[2]/span').click()

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="current-status-NEWLY_LICENSED"]').click()

driver.implicitly_wait(2)

#driver.find_element_by_xpath('//*[@id="current-status"]/fieldset/div/label[1]/span').click()
#driver.find_element_by_xpath('//*[@id="current-status"]/fieldset/div/label[1]/span/span[2]').click()

driver.implicitly_wait(2)

#driver.find_element_by_xpath('//*[@id="current-status"]/fieldset/div/label[1]/span/span[1]').click()
#//*[@id="current-status"]/fieldset/div/label[1]/span


#driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="new-policy-start-next"]').click()

# driver.implicitly_wait(5)

time.sleep(15)


