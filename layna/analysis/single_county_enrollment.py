import requests, json
import bs4
import csv

list_page_url = 'https://hfs.illinois.gov/info/factsfigures/program-enrollment/bond.html'
req = requests.get(list_page_url)

soup = bs4.BeautifulSoup(req.text, 'html.parser')

table = soup.find_all ('table')[2]

rows = table.find_all('tr')
headers = ('Year 2020', 'Year 2021', 'Year 2022', 'Year 2023', 'Year 2024')

print(headers)

output_file = open('bond_totalenrollment.csv','w') # file ready for writing

output_csv = csv.writer(output_file) # turns file into a csv

output_csv.writerow(headers) # writing header row


for row in rows[1:]:
    cells = row.find_all('td')  # Check if cells list is not empty before accessing elements

    if cells:
        year_2020 = cells[0].text.strip().replace('.', ',')
        year_2021 = cells[1].text.strip().replace('.', ',')
        year_2022 = cells[2].text.strip().replace('.', ',')
        year_2023 = cells[3].text.strip().replace('.', ',')
        year_2024 = cells[4].text.strip().replace('.', ',')
        data_out = [year_2020, year_2021, year_2022, year_2023, year_2024]

        output_csv.writerow(data_out) # writing data rows

output_file.close() 
