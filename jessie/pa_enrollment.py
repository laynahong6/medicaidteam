import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

url ='https://data.pa.gov/resource/2ght-hfn9.json'
response = requests.get(url)
content = response.text
data = json.loads(content)

print(data[-1])

df = pd.DataFrame(data)

# exclude statewide data
df = df[df['county_name'] != 'Statewide']

print(df.head(10))

print(df[['year','county_cd','county_name', 'ma_individuals', 'ma_children']])

# change text format to number to plot 
df['ma_individuals'] = pd.to_numeric(df['ma_individuals'], errors='coerce')
df['ma_children'] = pd.to_numeric(df['ma_children'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# filter to only include years 2015-2025
df_filtered_years = df[(df['year'] >= 2015) & (df['year'] <= 2025)].copy()

plt.figure(figsize=(12, 8))
plt.scatter(df_filtered_years['year'], df_filtered_years['ma_individuals'], color='blue', label='MA Individuals')

plt.xlabel('Year')
plt.ylabel('Enrollment')
plt.title('PA Medical Assistance Enrollment(2015-2025)')
plt.legend(['Individuals (21+) receiving MA'])
plt.show()

# make chart interactive
fig = px.scatter(df_filtered_years, x='date', y='ma_individuals', color='county_name',
                 labels={'date':'Year', 'ma_individuals':'Enrollment', 'county_name': 'County'},
                 title='PA Medicaid Enrollment by County (2015-2025)')

# center the title
fig.update_layout(title_x=0.5)

# add subheading
fig.add_annotation(
    text="Pennsylvania adults' (21+) enrollment in Medicaid, or medical assistance, remain generally stable with slight fluctuations in the last decade.",
    showarrow=False,
    xref="paper", yref="paper",
    x=0.5, y=1.05,
    align="center",
    xanchor="center",
    yanchor="top",
    font=dict(size=14)
)

# add source
fig.add_annotation(
    text="Source: <a href='https://data.pa.gov/Human-Services/Medical-Assistance-Enrollment-July-2003-Current-Mo/2ght-hfn9/about_data'>" \
    "Pennsylvania Department of Human Services</a>",
    xref="paper", yref="paper",
    x=1, y=-0.1,
    showarrow=False,
    xanchor="right",
    yanchor="bottom",
    font=dict(size=14, color="gray"),
)
fig.show()