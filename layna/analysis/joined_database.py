import pandas as pd 

df1 = pd.read_csv("layna/csv files/county_enrollment.csv")
df2 = pd.read_csv("layna/csv files/county_population.csv")

merged = pd.merge(df1, df2, on = "County Name", how="inner")

merged["Percentage"] = (merged ["2024 Enrollment"] / merged ["2024 Population Estimate"]) * 100

columns_to_keep = ["County Name", "2024 Enrollment", "2024 Population Estimate", "Percentage"]

merged_filtered = merged [columns_to_keep]

merged_filtered.to_csv("joined_output.csv", index=False)