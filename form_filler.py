from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GOOGLE_FORM_URL="https://docs.google.com/forms/d/e/1FAIpQLSeyeFL5phf2RwXiBdixus3jr_RkkXrYg40B5L_1PYUyzQJ75Q/viewform?usp=sf_link"

class Form_Filler():
    """
    A class used handle a Google From
    ...
    Attributes
    ----------
    None

    Methods
    -------
    fill_form(new_address, new_price, new_url)
        Fills the form with the data received in parameters and sends
    go_to_next_sheet()
        Goes to the next form
    close_browser()
        Closes the active browser
    """
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
        """
        Fills a Google form with the data received as parameters
        :param new_address: address of the property
        :param new_price: price of the property
        :param new_url: url with a description of the property
        :return: N/A
        """
        text_inputs = self.driver.find_elements(By.CLASS_NAME, value="whsOnd")
        text_inputs[0].send_keys(new_address)
        text_inputs[1].send_keys(new_price)
        text_inputs[2].send_keys(new_url)

        send_button = self.driver.find_element(By.CLASS_NAME, value="NPEfkd")
        send_button.click()

        #allow some time for the next page to load after the button click
        time.sleep(1)

    def go_to_next_sheet(self):
        """
        Moves to the next page
        :return: N/A
        """
        next_link = self.driver.find_element(By.CSS_SELECTOR, value="a")
        next_link.click()

    def close_browser(self):
        """
        Closes the browser
        :return: N/A
        """
        self.driver.quit()







