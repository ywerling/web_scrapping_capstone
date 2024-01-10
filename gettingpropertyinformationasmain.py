# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
import requests
from bs4 import BeautifulSoup
import re

ZILLOW_CLONE_URL="https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_CLONE_URL)
zillow_html = response.text
soup = BeautifulSoup(zillow_html, 'html.parser')

#find all rental prices
prices = soup.find_all(attrs={"data-test":"property-card-price"})
#print(prices)
price_list = []
for price in prices:
    price_list.append(f"${re.sub(r"[^0-9]",'',price.text.split()[0])}")
print(price_list)

#find all addresses
addresses = soup.find_all(attrs={"data-test":"property-card-addr"})
address_list = []
for address in addresses:
#    print(address.text.strip())
    address_list.append(address.text.strip())

#find all property links
links_list=[]
#links = soup.find_all('a', href=True, attrs={"data-test":"property-card-link"})
links = soup.find_all('a', href=True, class_="property-card-link")
for link in links:
#    print(link['href'])
    links_list.append(link['href'])



