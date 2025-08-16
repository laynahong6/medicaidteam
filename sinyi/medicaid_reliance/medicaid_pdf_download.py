from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

#Read all Illinois rural hospital IDs
csv_path = '/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/Il_rural_hospitals.csv'
df = pd.read_csv(csv_path)
id_list = df['ID'].astype(str).str.strip().tolist()

#Set up Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

#Fetch HFS website
driver = webdriver.Chrome(options=chrome_options)
hfs_url = 'https://hfs.illinois.gov/medicalproviders/costreports/2023medicarehospitalcostreports.html'
driver.get(hfs_url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source,'html.parser')
driver.quit()

#Extract PDF links
links = soup.find_all('a', href=True)
pdf_candidates = [link['href'] for link in links if link['href'].endswith('.pdf')]

print("🔍 所有 PDF 檔名前 10 個：")
for href in pdf_candidates[:10]:
    print(os.path.basename(href))

pdf_links = []
for href in pdf_candidates:
    filename = os.path.basename(href)
    for hospital_id in id_list:
        if filename.startswith(hospital_id):
            full_url = requests.compat.urljoin(hfs_url, href)
            pdf_links.append((hospital_id, filename, full_url))
            print(f"Matched: {hospital_id} to {filename}")
            break

print (f"Found {len(pdf_links)} matching PDFs.")

#Download the matching PDFs
output_dir = 'rural_hospital_costs_pdfs'
os.makedirs(output_dir, exist_ok=True)

for hospital_id, filename, pdf_url in pdf_links:
    print(f"Downloading for ID {hospital_id}")
    try:
        pdf_response = requests.get(pdf_url)
        pdf_response.raise_for_status()
        with open(os.path.join(output_dir, filename),'wb') as f:
            f.write(pdf_response.content)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")