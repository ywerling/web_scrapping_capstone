import requests
from bs4 import BeautifulSoup
import re

ZILLOW_CLONE_URL="https://appbrewery.github.io/Zillow-Clone/"

class Zillow():
    def __init__(self):
        response = requests.get(ZILLOW_CLONE_URL)
        zillow_html = response.text
        self.soup = BeautifulSoup(zillow_html, 'html.parser')

    def get_prices(self):
        # prices are tagged with the attribute value property-card-price
        prices = self.soup.find_all(attrs={"data-test": "property-card-price"})
        price_list = []
        for price in prices:
            # ensure that the prices follow the same format and remove unwanted characters
            price_list.append(f"${re.sub(r"[^0-9]", '', price.text.split()[0])}")
        return(price_list)

    def get_links(self):
        links_list = []
        links = self.soup.find_all('a', href=True, class_="property-card-link")
        for link in links:
            links_list.append(link['href'])
        return links_list

    def get_adddresses(self):
        addresses = self.soup.find_all(attrs={"data-test": "property-card-addr"})
        address_list = []
        for address in addresses:
            address_list.append(address.text.strip())
        return address_list


