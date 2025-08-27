import pandas as pd 

# reading both csv files 

df1 = pd.read_csv("layna/csv files/county_enrollment.csv")
df2 = pd.read_csv("layna/csv files/county_population.csv")

merged = pd.merge(df1, df2, on = "County Name", how="inner")

# creating new column to calculate percentage ((enrollment / population)*100) 

merged["Percentage"] = (merged ["2024 Enrollment"] / merged ["2024 Population Estimate"]) * 100

# formats number to express as a percentage 

merged['Percentage'] = merged['Percentage'].apply( lambda x : str(x) + '%')

# keeping only the year 2024 

columns_to_keep = ["County Name", "2024 Enrollment", "2024 Population Estimate", "Percentage"]

merged_filtered = merged [columns_to_keep]

merged_filtered.to_csv("joined_output.csv", index=False)