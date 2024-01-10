# this file is depreacted, was used to fill in the form from main.py this has been replaced by objects
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GOOGLE_FORM_URL="https://docs.google.com/forms/d/e/1FAIpQLSeyeFL5phf2RwXiBdixus3jr_RkkXrYg40B5L_1PYUyzQJ75Q/viewform?usp=sf_link"
#ensure windows stays open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrome_options)
driver.get(GOOGLE_FORM_URL)

#allow the page to load
time.sleep(1)

text_inputs=driver.find_elements(By.CLASS_NAME, value="whsOnd")
# for text_input in text_inputs:
#     text_input.send_keys("test")
text_inputs[0].send_keys("address")
text_inputs[1].send_keys("$2000")
text_inputs[2].send_keys("httpq")

send_button=driver.find_element(By.CLASS_NAME, value="NPEfkd")
send_button.click()

time.sleep(1)

next_link=driver.find_element(By.CSS_SELECTOR, value="a")
next_link.click()
