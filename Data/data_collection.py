from pybaseball import batting_stats, statcast_batter, playerid_lookup
import pandas as pd

# Get multiple years of batting stats
batting_stats_df = pd.concat([
    batting_stats(2023),
    batting_stats(2022),
    batting_stats(2021),
    batting_stats(2020), # COVID YEAR
    batting_stats(2019)
])

batting_stats_df.to_csv('battings_stats_2019_2023.csv')

