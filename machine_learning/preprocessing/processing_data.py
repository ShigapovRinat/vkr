import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

raw_players_match = pd.read_csv('../players/all_data/raw_players_match.csv')

zero_list = [np.NaN, '-', '0', '0.0']
players_match = raw_players_match[~raw_players_match['TOI'].isin(zero_list)].copy()
players_match = players_match[
    ~((players_match['Date'] == '11 Jan 2019') & (players_match['Teams'] == 'Slovan - Vityaz'))]

players_match = players_match[~(players_match['Score'] == '(-:-)')]


def icetime_fix(icetime):
    time_list = icetime.split(':')

    if len(time_list) == 2:
        return icetime

    else:
        minutes = 0
        seconds = int(time_list[0])
        while seconds >= 60:
            minutes += 1
            seconds -= 60
        return f'{minutes}:{seconds}'


def icetime_seconds(icetime):
    time_list = icetime.split(':')
    minutes = int(time_list[0])
    seconds = int(time_list[1])
    return minutes * 60 + seconds


players_match['Year'] = players_match['Season'].apply(lambda x: x[-9:])
players_match['Season'] = players_match['Season'].apply(lambda x: x[:-10])

players_match['Home_score'] = players_match['Score'].apply(lambda x: x.split(' ')[0].split(':')[0])
players_match['Away_score'] = players_match['Score'].apply(lambda x: x.split(' ')[0].split(':')[1])

players_match['Length'] = players_match['Score'].apply(lambda x: (x + ' ').split(' ')[1])

players_match['Home_team'] = players_match['Teams'].apply(lambda x: x.split('-')[0].split('(')[0].strip())
players_match['Away_team'] = players_match['Teams'].apply(lambda x: x.split('-')[1].split('(')[0].strip())

players_match['Role'] = players_match['Teams'].apply(lambda x: (x + '( ').split('(')[1][0])

players_match['TOI'] = players_match['TOI'].apply(icetime_fix)
players_match['TOI_seconds'] = players_match['TOI'].apply(icetime_seconds)

length_dict = {'': 'Standard', 'ОТ': 'Overtime', 'Б': 'Shootouts'}
players_match['Length'] = players_match['Length'].map(length_dict)
role_dict = {' ': 'Player', 'а': 'Assistant', 'к': 'Captain', 'a': 'Assistant', 'c': 'Captain',
             'K': 'Captain', 'k': 'Captain', 'К': 'Captain', 'А': 'Assistant', 'A': 'Assistant'}
players_match['Role'] = players_match['Role'].map(role_dict)

dynamo_list = ['Dynamo M', 'OHC Dynamo M', 'HC Dynamo M', 'Dynamo Msk']
players_match['Home_team'] = players_match['Home_team'].replace(to_replace=dynamo_list, value='Dynamo Msk')
players_match['Away_team'] = players_match['Away_team'].replace(to_replace=dynamo_list, value='Dynamo Msk')

short_names = list(players_match['Home_team'].unique())
short_names.sort()

long_names = ['Amur (Khabarovsk)', 'Dinamo (Minsk)', 'Lokomotiv (Yaroslavl)', 'Traktor (Chelyabinsk)', 'CSKA (Moscow)',
              'Salavat Yulaev (Ufa)', 'Spartak (Moscow)', 'Lada (Togliatti)', 'Metallurg (Novokuznetsk)',
              'Avtomobilist (Ekaterinburg)', 'Metallurg (Magnitogorsk)', 'Neftekhimik (Nizhnekamsk)',
              'Atlant (Moscow Region)', 'Avangard (Omsk)', 'Jokerit (Helsinki)', 'Vityaz (Moscow Region)',
              'Sibir (Novosibirsk Region)', 'SKA (Saint Petersburg)', 'Dynamo (Moscow)', 'Admiral (Vladivostok)',
              'HC Sochi (Sochi)', 'Ugra (Khanty-Mansiysk)', 'Donbass (Donetsk)', 'Severstal (Cherepovets)',
              'Ak Bars (Kazan)', 'Medvescak (Zagreb)', 'Barys (Nur-Sultan)', 'Dinamo (Riga)', 'Khimik (Voskresensk)',
              'Torpedo (Nizhny Novgorod Region)', 'Kunlun Red Star (Beijing)', 'HC MVD (Moscow Region)', 'Lev (Praha)',
              'Slovan (Bratislava)', 'Lev (Poprad)']
long_names.sort()

team_names = dict(zip(short_names, long_names))

players_match['Home_team'] = players_match['Home_team'].map(team_names)
players_match['Away_team'] = players_match['Away_team'].map(team_names)

team_dict = players_match.groupby('Team')['Home_team'].agg(pd.Series.mode).to_dict()
players_match['Team_name'] = players_match['Team'].map(team_dict)

players_match['Winner'] = np.where(players_match['Home_score'] > players_match['Away_score'],
                                   players_match['Home_team'], players_match['Away_team'])

players_match['Match_id'] = players_match.groupby(['Date', 'Home_team']).ngroup() + 1

players_match.drop(['Teams', 'Score'], axis=1, inplace=True)

columns = ['URL', 'Player name', 'Position', 'IDSeason', 'Team', 'Match_id', 'Season', 'Year', 'Team_name', '№', 'Role',
           'Date', 'Home_team', 'Away_team', 'Home_score', 'Away_score', 'Winner', 'Length', 'G', 'Assists', 'PTS',
           '+/-', '+', '-', 'PIM', 'ESG', 'PPG', 'SHG', 'OTG', 'GWG', 'SDS', 'SOG', '%SOG', 'FO', 'FOW', '%FO',
           'TOI', 'TOI_seconds', 'SFT', 'HITS', 'BLS', 'FOA', 'W', 'L', 'SOP', 'GA', 'Sv', '%Sv', 'GAA', 'SO']
players_match = players_match[columns]

header = ['Profile', 'Player', 'Position', 'Season_id', 'Team_id', 'Match_id', 'Season', 'Year', 'Team', 'Number',
          'Role',
          'Date', 'Home_team', 'Away_team', 'Home_score', 'Away_score', 'Winner', 'Length', 'Goals', 'Assists',
          'Points',
          'Plus_minus', 'Plus', 'Minus', 'Penalties', 'Goals_even', 'Goals_powerplay', 'Goals_shorthanded',
          'Goals_overtime',
          'Game_winning_goals', 'Game_winning_shootouts', 'Shots', 'Shots_percentage', 'Faceoffs', 'Faceoffs_won',
          'Faceoffs_percentage', 'Icetime', 'Icetime_seconds', 'Shifts', 'Hits', 'Shots_blocked', 'Penalties_against',
          'Wins', 'Losses', 'Shootouts', 'Goals_against', 'Saves', 'Saves_percentage', 'Goals_against_average',
          'Shutouts']
players_match.columns = header

players_object = ['Season_id', 'Team_id', 'Match_id', 'Number']
players_match[players_object] = players_match[players_object].astype('object')

players_match['Date'] = pd.to_datetime(players_match['Date'])

forward_match = players_match[players_match['Position'] == 'forward'].copy()
defense_match = players_match[players_match['Position'] == 'defense'].copy()
goaltender_match = players_match[players_match['Position'] == 'goaltender'].copy()

forward_match.drop(['Wins', 'Losses', 'Shootouts', 'Goals_against', 'Saves', 'Saves_percentage',
                    'Goals_against_average', 'Shutouts'], axis=1, inplace=True)

forward_int = ['Home_score', 'Away_score', 'Goals', 'Assists', 'Points', 'Plus_minus', 'Plus', 'Minus',
               'Penalties', 'Goals_even', 'Goals_powerplay', 'Goals_shorthanded', 'Goals_overtime',
               'Game_winning_goals', 'Game_winning_shootouts', 'Shots', 'Faceoffs', 'Faceoffs_won']
forward_match[forward_int] = forward_match[forward_int].astype('int')

forward_match['Shifts'] = forward_match['Shifts'].astype('float').astype('int')

forward_float = ['Shots_percentage', 'Faceoffs_percentage']
forward_match[forward_float] = forward_match[forward_float].replace('-', np.NaN).astype('float')
forward_match.head()

defense_match.drop(['Wins', 'Losses', 'Shootouts', 'Goals_against', 'Saves', 'Saves_percentage',
                    'Goals_against_average', 'Shutouts'], axis=1, inplace=True)

defense_int = ['Home_score', 'Away_score', 'Goals', 'Assists', 'Points', 'Plus_minus', 'Plus', 'Minus',
               'Penalties', 'Goals_even', 'Goals_powerplay', 'Goals_shorthanded', 'Goals_overtime',
               'Game_winning_goals', 'Game_winning_shootouts', 'Shots', 'Faceoffs', 'Faceoffs_won']
defense_match[defense_int] = defense_match[defense_int].astype('int')

defense_match['Shifts'] = defense_match['Shifts'].astype('float').astype('int')

defense_float = ['Shots_percentage', 'Faceoffs_percentage']
defense_match[defense_float] = defense_match[defense_float].replace('-', np.NaN).astype('float')
defense_match.head()

goaltender_match.drop(['Points', 'Plus_minus', 'Plus', 'Minus', 'Goals_even', 'Goals_powerplay', 'Goals_shorthanded',
                       'Goals_overtime', 'Game_winning_goals', 'Game_winning_shootouts', 'Shots_percentage',
                       'Faceoffs', 'Faceoffs_won', 'Faceoffs_percentage', 'Shifts', 'Hits', 'Shots_blocked',
                       'Penalties_against'],
                      axis=1, inplace=True)

goaltender_int = ['Home_score', 'Away_score', 'Goals', 'Assists', 'Penalties', 'Shots', 'Wins', 'Losses', 'Shootouts',
                  'Goals_against', 'Saves', 'Shutouts']
goaltender_match[goaltender_int] = goaltender_match[goaltender_int].astype('int')

goaltender_float = ['Saves_percentage', 'Goals_against_average']
goaltender_match[goaltender_float] = goaltender_match[goaltender_float].replace('-', np.NaN).astype('float')
goaltender_match.head()

forward_match.to_csv('forwards_match.csv', encoding='utf8', index=False)
defense_match.to_csv('defenses_match.csv', encoding='utf8', index=False)
goaltender_match.to_csv('goaltenders_match.csv', encoding='utf8', index=False)
