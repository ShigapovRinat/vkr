import numpy as np
import pandas as pd


if __name__ == '__main__':
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)

    columns_read = ['URL', 'Position']
    df = pd.read_csv('players/raw_players_match.csv', usecols=columns_read).drop_duplicates()
    df2 = pd.read_csv('players/raw_players_info.csv', usecols=columns_read).drop_duplicates()

    print(df.groupby('Position').count())
    print(df2.groupby('Position').count())

    columns_read = ['Team_id', 'Team']
    df = pd.read_csv('../players/forwards_match.csv', usecols=columns_read).drop_duplicates()
    print(df)
    print(df.count())

    df = pd.read_csv('../players/forwards_match.csv')
    df2 = pd.read_csv('../players/defenses_match.csv')
    df3 = pd.read_csv('../players/goaltenders_match.csv')
    seasons = ['2014/2015', '2015/2016', '2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021', '2021/2022']
    new_seasons = df[df['Year'].isin(seasons)].copy()
    new_seasons2 = df2[df2['Year'].isin(seasons)].copy()
    new_seasons3 = df3[df3['Year'].isin(seasons)].copy()
    new_seasons.to_csv('forwards_match_after_2014.csv', encoding='utf8', index=False)
    new_seasons2.to_csv('defenses_match_after_2014.csv', encoding='utf8', index=False)
    new_seasons3.to_csv('goaltenders_match_after_2014.csv', encoding='utf8', index=False)

    df = pd.read_csv('../players/after_2014/forwards_match_after_2014.csv')
    df2 = pd.read_csv('../players/after_2014/defenses_match_after_2014.csv')
    df3 = pd.read_csv('../players/goaltenders_match.csv')

    # print(df.describe())

    df = df.assign(Rating=((df.Goals * 5.54 + df.Assists * 4.28 + df.Plus * 2.47 +
                           df.Minus * (-2.37) + df.Penalties * (-0.65) + df.Shots * 0.47 +
                           df.Hits * 0.27 + df.Shots_blocked * 0.58 + df.Penalties_against * 0.82)))

    print(df.head())
    df.to_csv('forwards_match_with_rating.csv', encoding='utf8', index=False)

    df2 = df2.assign(Rating=((df2.Goals * 2.88 + df2.Assists * 4.09 + df2.Plus * 2.13 +
                              df2.Minus * (-2.06) + df2.Penalties * (-0.57) + df2.Shots * 0.22 +
                              df2.Hits * 0.29 + df2.Shots_blocked * 0.24 + df2.Penalties_against * 1.83)))

    print(df2.head())
    df2.to_csv('defenses_match_with_rating_int.csv', encoding='utf8', index=False)
