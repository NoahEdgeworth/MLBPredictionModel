import pandas as pd
import numpy as np

# Load cleaned Data
df = pd.read_csv('../Data/processed/clean_batting_stats.csv')

# Basic summary stats
print('Dataset Overview:')
print('-----------------')
print(f'Number of players: {len(df)}')
print(f'Number of unique players: {df["Name"].nunique()}')
print(f'Years covered: {df["Season"].min()} to {df["Season"].max()}')

# Key batting stats
print('\nKey Statistics Summary:')
print('-----------------------')
print(df[['AVG','OBP','SLG','HR','RBI','PA']].describe())

# League distribution
print('\nLeague Distribution:')
print('------------------------')
print(df['Team'].value_counts().head())

# Check for any remaining missing values
print('\nMissing Values:')
print('----------------')
print(df.isnull().sum()[df.isnull().sum() > 0])