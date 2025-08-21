import pandas as pd 
import csv
from rapidfuzz import process, fuzz # string matching library for python 

df1 = pd.read_csv("layna/county_enrollment.csv")
df2 = pd.read_csv("layna/county_population.csv")

col1 = df1.columns[0]
col2 = df2.columns[0]

choices = df2[col2].tolist()

def get_best_match(name, choices, score_cutoff=80):
    lower_choices = {c.lower(): c for c in choices}
    match = process.extractOne(name.lower(), lower_choices.keys(), scorer=fuzz.ratio, score_cutoff=score_cutoff)
    return lower_choices[match[0]] if match else name

df1[col1] = df1[col1].apply(lambda x: get_best_match(x, choices))

df1.rename(columns={col1:col2}, inplace=True)

df1.to_csv('FIXED_county_enrollment.csv', index=False)