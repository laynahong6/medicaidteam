import requests, json
from bs4 import BeautifulSoup
import csv
import pandas as pd

list_page_url = 'https://hfs.illinois.gov/info/factsfigures/program-enrollment/countieslist.html'
base_url = 'https://hfs.illinois.gov/'
list_page = requests.get(list_page_url).text

soup = BeautifulSoup (list_page, 'html.parser')

table = soup.find ('table')

links = table.find_all ('a', href=True)

from urllib.parse import urljoin 
county_urls = [urljoin(base_url, link['href']) for link in links] # do same thing with python strings 

for county_url in county_urls: 
    print(county_url)

output_file = open('county_enrollment.csv','w') # file ready for writing

output_csv = csv.writer(output_file) # turns file into a csv

headers = ('County Name','2020 Enrollment', '2021 Enrollment', '2022 Enrollment', '2023 Enrollment', '2024 Enrollment')

output_csv.writerow(headers) # writing header row

all_rows =[]

for url in county_urls: 
    req = requests.get(url)
    req.raise_for_status() # tells you if something fails
    soup = BeautifulSoup (req.text, 'html.parser')

    table = soup.find_all ('table')[2]

    rows = table.find_all('tr')

    county_name = url.split('/')[-1].replace('.html','')

    for row in rows[1:]:
        cells = row.find_all('td')  # Check if cells list is not empty before accessing elements
        
        def clean_text(text): 
            return text.strip().replace('.','').replace(',','') # removes commas and periods 

        if cells:
            year_2020 = clean_text(cells[0].text)
            year_2021 = clean_text(cells[1].text)
            year_2022 = clean_text(cells[2].text)
            year_2023 = clean_text(cells[3].text)
            year_2024 = clean_text(cells[4].text)
            data_out = [county_name,year_2020, year_2021, year_2022, year_2023, year_2024]

            #  output_csv.writerow(data_out) # writing data rows

            all_rows.append(data_out)

all_rows.sort(key=lambda x: x[0].lower()) 

for row in all_rows:
    output_csv.writerow(row)

output_file.close() 

