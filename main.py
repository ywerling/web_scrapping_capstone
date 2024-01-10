from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import zillow
import form_filler

GOOGLE_FORM_URL="https://docs.google.com/forms/d/e/1FAIpQLSeyeFL5phf2RwXiBdixus3jr_RkkXrYg40B5L_1PYUyzQJ75Q/viewform?usp=sf_link"

properties_for_rent=zillow.Zillow()

# print(properties_for_rent.get_links())
# print(properties_for_rent.get_prices())
# print(properties_for_rent.get_adddresses())

properties_links=properties_for_rent.get_links()
properties_prices=properties_for_rent.get_prices()
properties_addresses=properties_for_rent.get_adddresses()

# print(len(properties_links))
# print(len(properties_prices))
# print(len(properties_addresses))

google_form=form_filler.Form_Filler()

# google_form.fill_form("hello","world","https://www.google.com")
# google_form.go_to_next_sheet()
# google_form.fill_form("zero","music","https://www.google.ph")
# google_form.close_browser()

for index in range(0,len(properties_addresses)):
    google_form.fill_form(properties_addresses[index], properties_prices[index], properties_links[index])
    google_form.go_to_next_sheet()

google_form.close_browser()

print("Results can be viewed in the following spreadsheet: https://docs.google.com/spreadsheets/d/1HS_flYOuagfJe5a13iMVckKEmq9TNWcdztUnWYPQf8k/edit?resourcekey#gid=194917281")

