import pandas as pd
import requests, json
from bs4 import BeautifulSoup
import csv

df = pd.read_csv ('layna/censusdata_ALL.csv')

illinois = df[df['STNAME'] == 'Illinois']

illinois_counties = illinois[illinois['CTYNAME'] != 'Illinois']

columns_to_keep = ['CTYNAME','ESTIMATESBASE2020','POPESTIMATE2020','POPESTIMATE2021','POPESTIMATE2022','POPESTIMATE2023','POPESTIMATE2024']
    
filtered_df = illinois_counties[columns_to_keep]

filtered_df.to_csv ('illinois_census',index=False)



