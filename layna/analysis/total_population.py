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
    'CTYNAME':'County Name',
    'POPESTIMATE2020':'2020 Population Estimate',
    'POPESTIMATE2021':'2021 Population Estimate',
    'POPESTIMATE2022':'2022 Population Estimate',
    'POPESTIMATE2023':'2023 Population Estimate',
    'POPESTIMATE2024':'2024 Population Estimate'
})

filtered_df['County Name'] = (
    filtered_df['County Name']
    .str.replace(r'\s*county\s*','', case=False, regex=True)
    .str.replace(' ', '', regex=False)  # remove spaces
    .str.replace('.', '', regex=False)  # remove periods
    .str.lower()                        # convert to lowercase
    .str.strip()                        # remove leading/trailing spaces just in case
                
                            )
sorted_df = filtered_df.sort_values(by="County Name")

sorted_df.to_csv ('county_population.csv',index=False)



