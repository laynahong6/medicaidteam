import pandas as pd 
import csv
from rapidfuzz import process # string matching library for python 

df1 = pd.read_csv("layna/county_enrollment.csv")
df2 = pd.read_csv("layna/county_population.csv")

def clean_county_name(name): 
    return ( 
        str(name).strip().lower()
        .replace ("county","")
        .replace(".", "")
        .replace("-", " ")
        .title()
    )

df1["county_clean"] = df1.iloc[:,0].apply(clean_county_name)
df2["county_clean"] = df2.iloc[:,0].apply(clean_county_name)

counties_master = df2 ["county_clean"].unique()

def match_county(name): 
    match, score, _ = process.extract0ne (name, counties_master, score_cutoff=80)
    return match if match else name 

df1["county_clean"] = df1 ["county_clean"].apply(match_county)

merged = pd.merge(df1, df2, on="county_clean", how = "outer")

merged.to_csv("merged_counties.csv", index=False)
