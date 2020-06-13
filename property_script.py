from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')


driver.get('https://libertymutual.com/homeowners-insurance')

driver.maximize_window()
driver.find_element_by_xpath('//*[@id="quote-zipCode-input"]').click
driver.find_element_by_xpath('//*[@id="quote-zipCode-input"]').send_keys('03878')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="rentersQuteForm"]/div/div[3]/button').click()

driver.implicitly_wait(100)
try:
    time.sleep(10)
    ok =  driver.find_element_by_xpath('//*[@id="discount-marketing-modal"]/footer/div[1]/div/button')
    ActionChains(driver).move_to_element(ok).pause(1).click(ok).perform()
    time.sleep(3)
except:
    pass
driver.implicitly_wait(100)

driver.find_element_by_xpath('//*[@id="fullAddress-insuredLocation-0"]/span[2]/input').click()
driver.find_element_by_xpath('//*[@id="fullAddress-insuredLocation-0"]/span[2]/input').clear()
driver.find_element_by_xpath('//*[@id="fullAddress-insuredLocation-0"]/span[2]/input').send_keys(
    "111 Tri city RD, Somersworth, NH, 03878")
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="additionalStreetAddress-insuredLocation-0"]/span[2]/input').click()
driver.find_element_by_xpath('//*[@id="additionalStreetAddress-insuredLocation-0"]/span[2]/input').clear()
driver.find_element_by_xpath('//*[@id="additionalStreetAddress-insuredLocation-0"]/span[2]/input').send_keys(
    '111')
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="currentAddressSameAsLocationAddressIndicator-insured-0"]/div[2]/div/div[1]/label').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="nextButton-0"]').click()
driver.implicitly_wait(15)

driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='First Name'])[1]/following::input[1]").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='First Name'])[1]/following::input[1]").clear()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='First Name'])[1]/following::input[1]").send_keys(
    "xxtestxx")
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Last Name'])[1]/following::input[1]").click()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Last Name'])[1]/following::input[1]").clear()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Last Name'])[1]/following::input[1]").send_keys(
    "xxtestxx")
driver.implicitly_wait(1)
driver.find_element_by_name("month").click()
driver.implicitly_wait(1)
Select(driver.find_element_by_name("month")).select_by_visible_text("July")
driver.find_element_by_name("month").click()
driver.find_element_by_name("day").click()
driver.find_element_by_name("day").clear()
driver.find_element_by_name("day").send_keys("16")
driver.find_element_by_name("year").click()
driver.find_element_by_name("year").clear()
driver.find_element_by_name("year").send_keys("1996")
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="phoneNumber-insured-0"]/span[2]/div/div/input').click()
driver.find_element_by_xpath('//*[@id="phoneNumber-insured-0"]/span[2]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="phoneNumber-insured-0"]/span[2]/div/div/input').send_keys("9898989898")
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="emailAddress-insured-0"]/span[2]/input').click()
driver.find_element_by_xpath('//*[@id="emailAddress-insured-0"]/span[2]/input').clear()
driver.find_element_by_xpath('//*[@id="emailAddress-insured-0"]/span[2]/input').send_keys("test.test@gmail.com")
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="nextButton-1"]').click()
driver.implicitly_wait(3)
Select(driver.find_element_by_id(
    "propertyCurrentlyInsuredCode-insuranceHistory-0_selectNode")).select_by_visible_text(
    "No, first time home buyer")
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="hasOtherLibertyMutualPolicies-insuranceHistory-0"]/div[2]/div/div[2]/label').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="claimLossIndicator-insuranceHistory-0"]/div[2]/div/div[2]/label').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="mortgageIndicator-quote-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="nextButton-0"]').click()
driver.implicitly_wait(15)

Select(driver.find_element_by_id("homeStyleSimplified-insuredLocation-0_selectNode")).select_by_visible_text("1 Story")

driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Approximate Year Built'])[1]/following::input[1]").click()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Approximate Year Built'])[1]/following::input[1]").clear()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Approximate Year Built'])[1]/following::input[1]").send_keys(
    "2015")
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Approximate Square Footage'])[1]/following::input[1]").click()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Approximate Square Footage'])[1]/following::input[1]").clear()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Approximate Square Footage'])[1]/following::input[1]").send_keys(
    "1000")

Select(driver.find_element_by_id("foundationType-insuredLocation-0_selectNode")).select_by_visible_text(
    "Basement Finished")

Select(driver.find_element_by_id("roofMaterial-insuredLocation-0_selectNode")).select_by_visible_text(
    "Concrete Tile")

Select(driver.find_element_by_xpath('//*[@id="policyStartDate-quote-0_selectNode"]')).select_by_visible_text(
    "August 10, 2020")

Select(driver.find_element_by_xpath(
    '//*[@id="propertyPurchaseDate-insuredLocation-0"]/div/label[1]/select')).select_by_visible_text('May')

Select(driver.find_element_by_xpath(
    '//*[@id="propertyPurchaseDate-insuredLocation-0"]/div/label[2]/select')).select_by_visible_text('2015')

# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='Full Address'])[1]/following::input[1]").click()
# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='Full Address'])[1]/following::input[1]").clear()
# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='Full Address'])[1]/following::input[1]").send_keys(
#     "111 Tri city RD, Somersworth, NH, 03878")
# driver.implicitly_wait(1)
# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='Apt/Unit #'])[1]/following::input[1]").click()
# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='Apt/Unit #'])[1]/following::input[1]").clear()
# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='Apt/Unit #'])[1]/following::input[1]").send_keys(
#     "110")
#
# Select(
#     driver.find_element_by_xpath('//*[@id="ageOfRoof-insuredLocation-0_selectNode"]')).select_by_visible_text(
#     '2015')

driver.find_element_by_xpath('//*[@id="nextButton-1"]').click()
driver.implicitly_wait(15)
Select(driver.find_element_by_xpath('//*[@id="primaryHeatingSource-insuredLocation-1_selectNode"]')).select_by_visible_text("Oil")
driver.find_element_by_xpath('//*[@id="primaryHeatingSource-insuredLocation-1_selectNode"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath(
    '//*[@id="secondaryHeatingSourceIndicator-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="swimmingPoolOwnership-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="trampolineOwnership-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="undergroundOilStorageTank-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="nextButton-0"]').click()
driver.implicitly_wait(15)

driver.find_element_by_xpath(
    '//*[@id="anyPhysicalConditionsExistIndicator-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath(
    '//*[@id="underConstructionIndicator-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="hasBoarders-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="hasBusinessOnPremises-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath(
    '//*[@id="animalIndicator-insuredLocation-0"]/div[2]/div/div[2]/label/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="nextButton-1"]').click()
driver.implicitly_wait(15)

driver.find_element_by_xpath('//*[@id="next-button"]').click()
driver.implicitly_wait(15)

Select(driver.find_element_by_xpath('//*[@id="employmentStatus-insured-0_selectNode"]')).select_by_visible_text(
    'Employed')
driver.implicitly_wait(1)
Select(driver.find_element_by_xpath(
    '//*[@id="highestEducationLevel-insured-0_selectNode"]')).select_by_visible_text('Bachelors')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="nextButton-0"]').click()
driver.implicitly_wait(15)

driver.find_element_by_xpath('//*[@id="socialSecurityNumber-insured-0"]/span[2]/div/div/input')


time.sleep(10)
driver.close()

