import pandas as pd
import requests
import pdfplumber
import io
import re
from tqdm import tqdm

##read the medicaid rural hospital list
df_targets = pd.read_csv("/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/combined_rural_hospital_list.csv")
df_targets ['Medicaid_ID'] = df_targets['Medicaid_ID'].astype(str)

## access the HFS link
df_all = pd.read_html("https://hfs.illinois.gov/medicalproviders/costreports/2023medicaidhospitalcaostreports.html")[0]
df_all['Extraced_ID'] = df_all['Report Link'].str.extract(r'23h(\d+)-JD\.pdf')
df_final_targets = pd.merge(df_targets, df_all, left_on="Medicaid_ID", right_on="Extracted_ID", how="inner")

#processing
results = []
for index, row in df_final_targets.iterrows():
    pdf_bytes = requests.get('https://hfs.illinois.gov' + row['Report Link']).content

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        table1_p2 = pdf.pages[1].extract_tables()[1]
        total_row_p1 = table1_p2[22]

        table2_p2 = pdf.page[1].extract_tables()[2]
        total_row_p2 = table2_p2[22]

        table_p8 = pdf.pages[7].extract_tables()[1]
        total_charges = table_p8[12][2]

        results.append({
            'Medicaid_ID': row['Medicaid_ID'],
            'Total Charges': total_charges,
            'Part1 Total Beds': total_row_p1[1],
            'Part1 Inpatient Days': total_row_p1[4],
            'Part2 Inpatient Days': total_row_p2[4]
            })
        
#export
pd.DataFrame(results).to_csv('final_list.csv',index=False)