# %%
import cloudscraper
import requests
from bs4 import BeautifulSoup


import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

css = ".olx-ad-card__content"


site = BeautifulSoup(scraper.get("https://www.olx.com.br/estado-sp?q=forno").text, "html.parser")