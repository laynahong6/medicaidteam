import requests
import pandas as pd

#Download list of all U.S. rural and urban hospitals
url = "https://www.shepscenter.unc.edu/download/28591/"
filename = "US_hospitals.xlsx"

response = requests.get(url)
response.raise_for_status #error if download failed

with open(filename, 'wb') as f:
    f.write(response.content)

#Read and convert to csv
df = pd.read_excel(filename)
df.to_csv("US_hospitals.csv", index=False)

#Filter for rural hospitals and export new csv
rural_df = df[
    (df['FORHP RURAL 2024'] == 'Rural') &
    (df['STATE'] == 'IL')
]
rural_df.to_csv ('Il_rural_hospitals.csv', index=False)