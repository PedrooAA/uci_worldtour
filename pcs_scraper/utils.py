import pandas as pd


def clean_calendar(df):
    df['Season'] = df['Season'].str[:4]
    df['First_Date'] = pd.to_datetime(df['Date'].str[:5] + '.' + df['Season'], format='%d.%m.%Y',
                                      errors='coerce')  # .dt.strftime('%d.%m')
    df['Last_Date'] = pd.to_datetime(df['Date'].str[8:13] + '.' + df['Season'], format='%d.%m.%Y',
                                     errors='coerce')  # .dt.strftime('%d.%m')
    df['Last_Date'] = df['Last_Date'].fillna(df['First_Date'])
    df['N_Stages'] = ((df['Last_Date'] - df['First_Date']).dt.days + 1)
    df['Race_Link'] = df['Link'].str.split('/').str[1]

    return df


Stages = ['stage-1', 'stage-2', 'stage-3', 'stage-4', 'stage-5', 'stage-6', 'stage-7', 'stage-8',
          'stage-9', 'stage-10', 'stage-11', 'stage-12', 'stage-13', 'stage-14', 'stage-15', 'stage-16',
          'stage-17', 'stage-18', 'stage-19', 'stage-20', 'stage-21']
race_name = []
stages = []


class RaceDicts:
    def __init__(self, df):
        self.df = df

    def n_stages_dict(self):
        df = clean_calendar(self.df)
        max_ = df.groupby('Race_Link')[['N_Stages']].max()

        n_stages = dict(zip(max_.index.tolist(), max_['N_Stages'].tolist()))
        return n_stages

    def generate_sr_dict(self, n_stages):

        for race, value in self.n_stages_dict().items():
            if value == n_stages:
                race_name.append(race)
                stages.append(Stages[:n_stages])
        sr_dict = dict(zip(race_name, stages))
        return sr_dict

    def generate_dicts(self):
        odr_dict = dict((k, v) for k, v in self.n_stages_dict().items() if v == 1)

        for n in range(2, 25):
            sr_dict = self.generate_sr_dict(n)

        return odr_dict, sr_dict


def selected_teams(df_teams, min_season):
    seasons = df_teams[df_teams.Season >= min_season]
    wtteams = seasons[seasons.Division == 'UCI WorldTeams']
    wtteams = wtteams.Team_Name.unique().tolist()
    ptteams = ['Alpecin-Deceuninck', 'Team Arkéa Samsic', 'TotalEnergies', 'Alpecin-Fenix', 'Circus - Wanty Gobert',
               'Team Total Direct Energie', 'Corendon - Circus', 'Israel Cycling Academy',
               'Wanty - Gobert Cycling Team', 'Wanty - Groupe Gobert', 'Direct Energie', 'Cofidis, Solutions Crédits',
               'Bora - Argon 18']
    foldedteams = ['Tinkoff', 'IAM Cycling', 'Team Katusha', 'Team Dimension Data', 'BMC Racing Team',
                   'Team Katusha Alpecin', 'NTT Pro Cycling', 'CCC Team', 'Team Qhubeka NextHash']
    teams = seasons[~seasons.Team_Name.isin(foldedteams)]
    teams = teams[teams.Team_Name.isin(wtteams + ptteams)]
    teams['Link'] = teams.Link.str.split('/').str[1]
    teams['Link'] = teams.Link.str.split('"').str[0]
    return teams


def team_list(df_teams, min_season, df_nations):
    teams = selected_teams(df_teams, min_season)
    nations = df_nations.Nation.unique().tolist()
    teams = teams.Team_Name.unique().tolist()
    return teams + nations






