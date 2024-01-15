import requests
from bs4 import BeautifulSoup
import re

ZILLOW_CLONE_URL="https://appbrewery.github.io/Zillow-Clone/"

class Zillow():
    """
    A class used to handle the webscrapping of the Zillow website

    Attributes
    ----------
    None

    Methods
    -------
    get_prices()
        Returns a list containing the prices found on the webpage

    get_links()
        Returns a list containing the links to properties found on the webpage

    get_adddresses()
        Returns a list containing the addresses of the properties found on the webpage
    """
    def __init__(self):
        """
        class initialization
        """
        response = requests.get(ZILLOW_CLONE_URL)
        zillow_html = response.text
        self.soup = BeautifulSoup(zillow_html, 'html.parser')

    def get_prices(self):
        """
        Gets the prices of the properties found
        :return: list of property prices
        """
        # prices are tagged with the attribute value property-card-price
        prices = self.soup.find_all(attrs={"data-test": "property-card-price"})
        price_list = []
        for price in prices:
            # ensure that the prices follow the same format and remove unwanted characters
            price_list.append(f"${re.sub(r"[^0-9]", '', price.text.split()[0])}")
        return(price_list)

    def get_links(self):
        """
        Gets the links to the properties found
        :return: list of property links
        """
        links_list = []
        links = self.soup.find_all('a', href=True, class_="property-card-link")
        for link in links:
            links_list.append(link['href'])
        return links_list

    def get_adddresses(self):
        """
        Gets the addresses of the properties found
        :return: list of property addresses
        """
        addresses = self.soup.find_all(attrs={"data-test": "property-card-addr"})
        address_list = []
        for address in addresses:
            address_list.append(address.text.strip())
        return address_list


