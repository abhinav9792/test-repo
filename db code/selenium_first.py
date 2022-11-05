from selenium import webdriver
import os


driver = webdriver.Chrome(executable_path='selenium/chrome_driver/chromedriver')
driver.implicitly_wait(8)
driver.get("https://www.seleniumeasy.com/") 
e =driver.find_element(by =by.LINK_TEXT,value="http://seleniumeasy.com/apachepoi-tutorials")
e.click()