import pandas as pd
import matplotlib.pyplot as plt
import os

# dataset url (filtered for illinois)
url = "https://data.medicaid.gov/dataset/6165f45b-ca93-5bb5-9d06-db29c692a360/data?conditions[0][property]=state_abbreviation&conditions[0][value]=IL&conditions[0][operator]=%3D&conditions[1][property]=total_medicaid_enrollment&conditions[1][value]=0&conditions[1][operator]=%3C%3E"

# loading dataset from url
df = pd.read_csv(url)

# grouping by reporting period and calculating average enrollment
il_summary = df.groupby("reporting_period")[["total_medicaid_enrollment"]].mean().reset_index()

# exporting results/summary as separate csv (for illinois enrollment over certain periods of time)
il_summary.to_csv("data/illinois_enrollment.csv", index=False)

# plotting the trends in results and create visualization figure
plt.figure(figsize=(10,6))
plt.plot(il_summary["reporting_period"], il_summary["total_medicaid_enrollment"], marker="o")
plt.title("Total Medicaid Enrollment in Illinois by Reporting Period")
plt.xlabel("Reporting Period")
plt.ylabel("Total Medicaid Enrollment")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/illinois_enrollment_trend.png")
plt.close()
