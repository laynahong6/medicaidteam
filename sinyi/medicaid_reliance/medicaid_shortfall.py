import os
import re
import fitz
import pandas as pd

#Define the phrase to find
def extract_medicaid_shortfall(text):
    pattern = r"Difference\s+between\s+net\s+revenue\s+and\s+costs\s+for\s+Medicaid\s+program.*?\n([\d,]+)"
    match = re.search(pattern,text,re.DOTALL | re.IGNORECASE)
    if match:
        raw = match.group(1).replace(",","")
        try:
            return int(raw)
        except:
            pass
    return None

pdf_folder = "/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/medicaid_reliance/rural_hospital_costs_pdfs"
results = []

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        pdf_id = filename[:6]
        medicaid_value = None
        page_info = "N/A"

        try:
            with fitz.open(pdf_path) as doc:
                for page_num, page in enumerate(doc, start=1):
                    text = page.get_text()
                    value = extract_medicaid_shortfall(text)
                    if value is not None:
                        medicaid_value = value
                        page_info = f"Page {page_num}"
                        break

        except Exception as e:
            print(f"⚠️ Error for {filename}: {e}")

        results.append({
            "ID": pdf_id,
            "Medicaid shortfall": medicaid_value,
            "Page_info": page_info
        })

#Export to csv
df = pd.DataFrame(results)
df.to_csv("medicaid_shortfall.csv", index=False)