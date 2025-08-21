import pandas as pd 
import csv
from rapidfuzz import process # string matching library for python 

df1 = pd.read_csv("layna/county_enrollment.csv", header=0)
df2 = pd.read_csv("layna/county_population.csv", header=0)

def clean_county_name(name): # function to clean up header names 
    return ( 
        str(name).strip().lower()
        .replace ("county","")
        .replace(".", "")
        .replace("-", " ")
        .title() # title case
    )

# the below uses rapidfuzz to find best matches between the two files

counties_master = df2[:,0].apply(clean_county_name).unique()

def match_county(name): 
    result = process.extractOne(cleaned, counties_master, score_cutoff=80)
    if result: 
        match, score, _ = result
        return match
    return cleaned

df1.iloc[:,0] = df1.iloc[:,0].apply(match_county)
df2.iloc[:,0] = df2.iloc[:,0].apply(clean_county_name) 

df1.to_csv("FIXED_county_enrollment.csv", index=False)

df2.to_csv("FIXED_county_population.csv", index=False)