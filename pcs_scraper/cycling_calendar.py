import pandas as pd
import re
from scraper import *

tours_dict = {'World Tour': 1,
              'Europe Tour': 13,
              'Pro Series': 26,
              'WC': 2,
              'Olympics': 3,
              'America Tour': 18,
              'Asia Tour': 12,
              'Africa Tour': 11,
              'Oceania Tour': 14}

raceclasses = ['1.UWT', '2.UWT', '1.Pro', '2.Pro', '1.HC', '2.HC', '1.1',
               '1.2', '2.1', '2.2', 'Olympics', 'WC', 'NC', 'CC']


class Calendar(Scraper):
    YEAR = 2022
    YEARS_BACK = 6

    def __init__(self):
        super().__init__(Calendar.YEAR, Calendar.YEARS_BACK)

    @staticmethod
    def get_url():
        cal_urls = []
        for tour in tours_dict.values():
            for y in range(int(Calendar.YEAR), int(Calendar.YEAR - (Calendar.YEARS_BACK + 1)), -1):
                url = 'https://www.procyclingstats.com/races.php?year=' + str(y) + '&circuit=' + str(
                    tour) + '&class=&filter=Filter'
                cal_urls.append(url)
        return cal_urls

    def get_calendar(self):
        cal_urls = self.get_url()
        race = []
        type_ = []
        year = []
        date = []
        race_link = []

        for tour in cal_urls[:]:
            Scraper.sleeper()
            soup = Scraper.download_soup(tour)

            calendar_table_tag = soup.find('table', class_='basic')
            calendar_table_element = calendar_table_tag.find_all('tr')

            url_split = tour.split('=')

            for i in calendar_table_element[1:]:
                if [t for t in raceclasses if t in i.text]:
                    race.append(str(i.find_all('td')[2].text.strip()))
                    type_.append(str(i.find_all('td')[4].text.strip()))
                    year.append(url_split[1])
                    date.append(str(i.find_all('td')[0].text.strip()))
                    race_link.append(str(i.find_all('a', href=re.compile('race/'))))

        results = pd.DataFrame({'Race': race, 'Class': type_, 'Season': year, 'Date': date, 'Link': race_link})
        return results.to_csv('Cycling_Calendar.csv', encoding='utf-8', index=True)


