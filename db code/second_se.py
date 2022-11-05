from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='selenium/chrome_driver/chromedriver')
driver.implicitly_wait(8)
driver.get("https://www.seleniumeasy.com/") 


WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (BY.CLASS_NAME,"text label"),#element filteration
        "completed!"#expected text
    )
)  