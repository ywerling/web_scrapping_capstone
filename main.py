import zillow
import form_filler

# gather property information from the Zillow website
properties_for_rent=zillow.Zillow()
properties_links=properties_for_rent.get_links()
properties_prices=properties_for_rent.get_prices()
properties_addresses=properties_for_rent.get_adddresses()

# fill the google form with the extracted data
google_form=form_filler.Form_Filler()
for index in range(0,len(properties_addresses)):
    google_form.fill_form(properties_addresses[index], properties_prices[index], properties_links[index])
    google_form.go_to_next_sheet()
google_form.close_browser()

print("Results can be viewed in the following spreadsheet: https://docs.google.com/spreadsheets/d/1HS_flYOuagfJe5a13iMVckKEmq9TNWcdztUnWYPQf8k/edit?resourcekey#gid=194917281")

