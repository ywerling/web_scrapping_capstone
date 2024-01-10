from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GOOGLE_FORM_URL="https://docs.google.com/forms/d/e/1FAIpQLSeyeFL5phf2RwXiBdixus3jr_RkkXrYg40B5L_1PYUyzQJ75Q/viewform?usp=sf_link"

class Form_Filler():
    def __init__(self):
        # ensure windows stays open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        #open the page in the browser
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get(GOOGLE_FORM_URL)

        # allow the page to load
        time.sleep(1)

    def fill_form(self, new_address, new_price, new_url):
        text_inputs = self.driver.find_elements(By.CLASS_NAME, value="whsOnd")
        text_inputs[0].send_keys(new_address)
        text_inputs[1].send_keys(new_price)
        text_inputs[2].send_keys(new_url)

        send_button = self.driver.find_element(By.CLASS_NAME, value="NPEfkd")
        send_button.click()

        #allow some time for the next page to load after the button click
        time.sleep(1)

    def go_to_next_sheet(self):
        next_link = self.driver.find_element(By.CSS_SELECTOR, value="a")
        next_link.click()

    def close_browser(self):
        self.driver.quit()







