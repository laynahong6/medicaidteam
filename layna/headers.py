import pandas as pd 
import csv
from rapidfuzz import process, fuzz # string matching library for python 

df1 = pd.read_csv("layna/county_enrollment.csv")
df2 = pd.read_csv("layna/county_population.csv")

col1 = df1.columns[0]
col2 = df2.columns[0]

choices = df2[col2].tolist()

# below is getting best case-insenstive match using rapidfuzz library 

def get_best_match(name, choices, score_cutoff=80):
    lower_choices = {c.lower(): c for c in choices} # makes a dictionary so lowercase name -> original name

    match = process.extractOne(
        name.lower(), # lowercase input version 
        lower_choices.keys(), # lowercase dictionary keys
        scorer=fuzz.ratio, 
        score_cutoff=score_cutoff # ignore bad matches
        ) 
    return lower_choices[match[0]] if match else name # in case of match, replace with df2 columns 

df1[col1] = df1[col1].apply(lambda x: get_best_match(x, choices)) # applies function to every county in df1

df1.rename(columns={col1:col2}, inplace=True) # renames first column in df1 to that in df2

df1_sorted = df1.sort_values(by="County Name")

df1_sorted.to_csv('FIXED_county_enrollment.csv', index=False)