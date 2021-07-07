#Scraping from Etsy, to take user reviews and all

from bs4 import BeautifulSoup
import requests

main_url = 'https://alixpress.com'
response = requests.get(main_url)

soup = BeautifulSoup(response, 'html')