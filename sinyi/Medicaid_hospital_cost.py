import requests
import pdfplumber
import pandas as pd
import io

## import the url of the PDF file of Medicaid hospital costs
pdf_url = "https://hfs.illinois.gov/content/dam/soi/en/web/hfs/medicalproviders/medicaidreimbursement/2023-medicaid-hospital-cost-reports/23FacilityID.pdf"
csv_path = "Medciaid_hospital_cost.csv"

## read the PDF
response = requests.get(pdf_url)
pdf_medicaidhospital = io.BytesIO(response.content)

## extract the table
all_rows = []
with pdfplumber.open(pdf_medicaidhospital) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        if tables:
            for tables in tables:
                all_rows.extend (tables)

## save as csv
df = pd.DataFrame (all_rows[1:], columns=all_rows[0])
df.to_csv(csv_path, index=False)

