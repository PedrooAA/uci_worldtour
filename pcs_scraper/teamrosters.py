import pandas as pd
from scraper import *
from utils import selected_teams

teams = selected_teams(pd.read_csv('Cycling_Teams.csv'), 2016)
url_names = teams.Link.to_list()
team_urls = ['https://www.procyclingstats.com/team/' + u for u in url_names]

def get_teamrosters():
    season = []
    teamname = []
    ridername = []
    duration = []

    for url in team_urls[:]:
        Scraper.sleeper()
        soup = Scraper.download_soup(url)

        teamroster_ul_tag = soup.find_all('ul', class_='list pad2')[2]
        teamroster_ul_element = teamroster_ul_tag.find_all('li')

        for i in teamroster_ul_element[:]:
            season.append(str(soup.find('span', class_='red hideIfMobile').text.strip()))
            teamname.append(str(soup.find('h1').text.strip()))
            # ridername.append(i.find_all('div')[1].text.strip())
            ridername.append(str(i.find('a')).split('"')[1])
            duration.append(str(i.find_all('div')[2].text.strip()))

    teamrosters = pd.DataFrame({'Season': season, 'Team_Name': teamname, 'Rider_Name': ridername, 'Duration': duration})
    return teamrosters.to_csv('Cycling_TeamRosters.csv', encoding='utf-8', index=True)
