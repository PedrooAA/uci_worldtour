import pandas as pd
from scraper import *
from utils import clean_calendar, RaceDicts, team_list


class RaceResults(Scraper):
    YEAR = 2022
    YEARS_BACK = 6

    def __init__(self, racetype):
        self.racetype = racetype
        if self.racetype not in ("gc", "sr", "odr"):
            raise ValueError("Supported racetypes entries are 'gc', 'sr' or 'odr'")
        super().__init__(RaceResults.YEAR, RaceResults.YEARS_BACK)

    def get_url(self):
        calendar = clean_calendar(pd.read_csv('Cycling_Calendar.csv'))
        odr_dict = RaceDicts(calendar).generate_dicts()[0]
        sr_dict = RaceDicts(calendar).generate_dicts()[1]
        race_urls = []
        if self.racetype == "gc":
            for race in sr_dict:
                for year in range(int(RaceResults.YEAR), int(RaceResults.YEAR - (RaceResults.YEARS_BACK + 1)), -1):
                    url = 'https://www.procyclingstats.com/race/' + str(race) + '/' + str(year) + '/gc/result/result'
                    race_urls.append(url)
        if self.racetype == "odr":
            for race in odr_dict:
                for year in range(int(RaceResults.YEAR), int(RaceResults.YEAR - (RaceResults.YEARS_BACK + 1)), -1):
                    url = 'https://www.procyclingstats.com/race/' + str(race) + '/' + str(year) + '/result'
                    race_urls.append(url)
        if self.racetype == "sr":
            for race in sr_dict:
                for stage in sr_dict[race]:
                    for year in range(int(RaceResults.YEAR), int(RaceResults.YEAR - (RaceResults.YEARS_BACK + 1)), -1):
                        url = 'https://www.procyclingstats.com/race/' + str(race) + '/' + str(year) + '/' + str(
                            stage) + '/result/result'
                        race_urls.append(url)
        return race_urls

    def get_results(self):
        race_urls = self.get_url()
        racename = []
        stage = []
        year = []
        date = []
        rank = []
        gc_rank = []
        team = []
        name = []

        for race in race_urls[:]:
            Scraper.sleeper()
            soup = Scraper.download_soup(race)

            try:

                if self.racetype == "gc":
                    race_table_tag = soup.find_all('table', class_='results basic moblist10')[1]
                if self.racetype == "odr":
                    race_table_tag = soup.find_all('table', class_='results basic moblist10')[0]
                if self.racetype == "sr":
                    race_table_tag = soup.find_all('table', class_='results basic moblist10')[0]
                table_element = race_table_tag.find_all('tr')
                infolist_tag = soup.find('ul', class_='infolist')

                url_split = race.split('/')

                for i in table_element[1:]:
                    teams = pd.read_csv('Cycling_Teams.csv')
                    nations = pd.read_csv('Cycling_Nations.csv')
                    if [t for t in team_list(teams, 2016, nations) if t in i.text]:
                        racename.append(url_split[4])
                        stage.append(str(soup.find('span', class_='blue').text))
                        year.append(str(soup.find('span', class_='hideIfMobile').text))
                        date.append(str(infolist_tag.find_all('li')[0].text))
                        rank.append(str(i.find_all('td')[0].text))
                        if self.racetype == "gc":
                            gc_rank.append(str("-"))
                            team.append(str(i.find_all('td')[7].text.strip()))
                            # team.append(str(i.find_all('a')[1].text.strip()))
                        if self.racetype == "odr":
                            gc_rank.append(str("-"))
                            team.append(str(i.find_all('td')[5].text.strip()))
                        if self.racetype == "sr":
                            gc_rank.append(str(i.find_all('td')[1].text))
                            team.append(str(i.find_all('td')[7].text.strip()))
                        name.append(str(i.find('a')).split('"')[1])
                        # name.append(i.find_all('td')[rider_n_td].text.strip())

            except (AttributeError, IndexError) as e:
                continue

        results = pd.DataFrame({'Race_Name': racename, 'Stage': stage, 'Name': name, 'Season': year,
                             'Date': date, 'Rank': rank, 'GC_Rank': gc_rank, 'Team_Name': team})

        return results.to_csv(str(self.racetype).upper() + '_Results.csv', encoding='utf-8', index=False)