import pandas as pd
import requests, json
from bs4 import BeautifulSoup
import csv

df = pd.read_csv ('layna/censusdata_ALL.csv')

illinois = df[df['STNAME'] == 'Illinois']

illinois_counties = illinois[illinois['CTYNAME'] != 'Illinois']

columns_to_keep = ['CTYNAME','POPESTIMATE2020','POPESTIMATE2021','POPESTIMATE2022','POPESTIMATE2023','POPESTIMATE2024']
    
filtered_df = illinois_counties[columns_to_keep]

filtered_df = filtered_df.rename(columns={
    'CTYNAME':'county_name',
    'POPESTIMATE2020':'2020',
    'POPESTIMATE2021':'2021',
    'POPESTIMATE2022':'2022',
    'POPESTIMATE2023':'2023',
    'POPESTIMATE2024':'2024'
})

filtered_df.to_csv ('county_population.csv',index=False)



