import requests
from bs4 import BeautifulSoup
import time
import random
from IPython.display import clear_output


class Scraper:
    def __init__(self, year, years_back):
        self.year = year
        self.years_back = years_back

    @staticmethod
    def download_soup(url):
        print('Starting request for: ' + url)
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            page = response.text
            soup = BeautifulSoup(page, 'html.parser')
            print('Successful request!')
            return soup
        else:
            print('Unsuccessful request, status code: ' + str(response.status_code))

    @staticmethod
    def sleeper():
        timer = 0.5 + 0.5 * random.random()
        time.sleep(timer)
        clear_output(wait=True)