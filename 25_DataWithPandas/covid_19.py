'''
Project to explore covid 19 data
using pandas
'''

import pandas as pd
import numpy as np
import os
import urllib
import urllib.request

url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
file_path = os.path.join('Data', 'Covid')

os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path, 'WHO-COVID-19-global-data.csv')
urllib.request.urlretrieve(url, csv_path)
df = pd.read_csv(csv_path)
# print(df)

# dfindex = df.index
# dfcols = df.columns

# print(dfindex)
# print(dfcols)
# # print(df.values)
# print(df.dtypes)
# print(df.shape)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.Country)
# or
# print(df['Country])
# print(df.County.unique)
# if there are trailing or leading spaces remove with:
# df.columns = [col.strip() for col in df.columns]

# Access data using .loc

# print(df.loc[1:4, 'Country'])
# print(df.loc[1:18, ['Country', 'New_cases']])
# print(df.Country == 'United States of America')
# print(df[df.Country == 'United States of America'])
# print(df.New_deaths > 1000)
# print(df.loc[df.New_deaths > 1000, ['Date_reported', 'New_deaths', 'Country']])

# Goes through max, min, sum etc.  All pretty basic stuff
print(df.loc[df.New_deaths.idxmax(), ['Date_reported', 'Country',
      'New_cases', 'New_deaths', 'Cumulative_deaths']])

# Add new column again pretty basic stuff

df['pct_cases'] = (df['New_cases'] / df['Cumulative_cases']) * 100
print(df.head())
