import pandas as pd
import numpy as np


def strip_rank(df_results):
    df_results['Rank'] = df_results['Rank'].str.strip()
    return df_results


def join_calendar(df_results):
    calendar = pd.read_csv('Cycling_Calendar.csv')
    calendar['Season'] = pd.to_numeric(calendar['Season'])
    df_results = strip_rank(df_results).merge(calendar.drop(['Link', 'First Date', 'Last Date',
                                                             'N_Stages', 'Date'], axis=1),
                                              left_on=['Race_Name', 'Season'],
                                              right_on=['Race Link', 'Season'], how='left')
    df_results = df_results[['Race', 'Race_Name', 'Season', 'Date', 'Week_Number', 'Class', 'Stage',
                             'Name', 'Team_Name', 'Rank', 'GC_Rank']]
    df_results = df_results.dropna()
    return df_results


def clean_name(df_results):
    df_results = join_calendar(df_results)
    df_results['Name'] = df_results['Name'].str[6:]
    df_results['Name'] = [i.replace('-', ' ') for i in df_results['Name']]
    df_results['Name'] = df_results['Name'].str.title()
    return df_results


def clean_rank(df_results):
    df_results = clean_name(df_results)
    df_results = df_results.replace({'Rank': {'OTL': '0', 'DNS': '0', 'DNF': '0', 'DSQ': '0', 'DF': '0'}})
    df_results['Rank'] = pd.to_numeric(df_results.Rank).astype(int)
    if df_results == sr_results:
        df_results = df_results.replace({'GC_Rank': {'-': '0'}})
        df_results['GC_Rank'] = df_results['GC_Rank'].fillna('0')
        df_results['GC_Rank'] = pd.to_numeric(df_results.GC_Rank).astype(int)
    else:
        pass
    return df_results


def replace_nations(df_results):
    df_results = clean_rank(df_results)
    team_roster = pd.read_csv('Cycling_TeamRosters.csv')

    team_roster = team_roster[['Season', 'Team_Name', 'Rider_Name', 'Week_Number_Start', 'Week_Number_End']]
    team_roster = team_roster.rename(columns={'Season': 'Season1', 'Team_Name': 'Team'})

    df_results_r = df_results.Name.values
    df_results_w = df_results.Week_Number.values
    df_results_s = df_results.Season.values

    team_roster_ws = team_roster.Week_Number_Start.values
    team_roster_we = team_roster.Week_Number_End.values
    team_roster_r = team_roster.Rider_Name.values
    team_roster_s = team_roster.Season1.values

    i, j = np.where((df_results_r[:, None] == team_roster_r) & (df_results_s[:, None] == team_roster_s) &
                    (df_results_w[:, None] >= team_roster_ws) & (df_results_w[:, None] <= team_roster_we))

    df_results = pd.DataFrame(np.column_stack([team_roster.values[j], df_results.values[i]]),
                      columns=team_roster.columns.append(df_results.columns))
    df_results = df_results.drop(columns=['Season1', 'Rider_Name', 'Week_Number_Start', 'Week_Number_End', 'Team_Name'])
    return df_results


def rename_(df_results):
    df_results = replace_nations(df_results)
    if df_results == odr_results:
        df_results.loc[(df_results["Class"] == 'NC') &
                       (df_results["Stage"] == 'Time trial'), ['Class']] = 'NC_ITT'
    else:
        pass
    return df_results