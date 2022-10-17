import pandas as pd
import re
from scraper import *


class Teams(Scraper):
    YEAR = 2022
    YEARS_BACK = 6

    def __init__(self):
        super().__init__(Teams.YEAR, Teams.YEARS_BACK)

    @staticmethod
    def get_url():
        teams_url = []
        for y in range(int(Teams.YEAR), int(Teams.YEAR - (Teams.YEARS_BACK + 1)), -1):
            url = 'https://www.procyclingstats.com/teams.php?year=' + str(y) + '&filter=Filter'
            teams_url.append(url)
        return teams_url

    def get_teams(self):
        teams_url = self.get_url()
        season = []
        division = []
        name = []
        link = []

        for url in teams_url[:]:
            Scraper.sleeper()
            soup = Scraper.download_soup(url)

            wtteam_ul_tag = soup.find_all('div', class_='mt20')[0]  # list fs14 columns2 mob_columns1
            wtteam_ul_element = wtteam_ul_tag.find_all('li')
            ptteam_ul_tag = soup.find_all('div', class_='mt20')[2]
            ptteam_ul_element = ptteam_ul_tag.find_all('li')

            url_split = url.split('=')

            for i in wtteam_ul_element[:]:
                season.append(url_split[1][:4])
                division.append(str(wtteam_ul_tag.find('h3').text))
                # name.append(str(i.find('a')).split('"')[1])
                name.append(str(i.find_all('div')[0].text.strip()))
                link.append(str(i.find_all('a', href=re.compile('team/'))))

            for i in ptteam_ul_element[:]:
                season.append(url_split[1][:4])
                division.append(str(ptteam_ul_tag.find('h3').text))
                # name.append(str(i.find('a')).split('"')[1])
                name.append(str(i.find_all('div')[0].text.strip()))
                link.append(str(i.find_all('a', href=re.compile('team/'))))

        teams = pd.DataFrame({'Season': season, 'Division': division, 'Team_Name': name, 'Link': link})
        return teams.to_csv('Cycling_Teams.csv', encoding='utf-8', index=True)


def get_nations():
    soup = Scraper.download_soup("https://www.procyclingstats.com/statistics/nations")

    nations_table_tag = soup.find('table', class_='basic')
    nations_element = nations_table_tag.find_all('tr')

    nation = []

    for i in nations_element[1:]:
        nation.append(str(i.find('a')).split('"')[1])

    nations = pd.DataFrame({'Nation': nation})
    nations['Nation'] = nations['Nation'].str[7:]
    nations['Nation'] = nations['Nation'].str.title()
    return nations.to_csv('Cycling_Nations.csv', encoding='utf-8', index=False)

