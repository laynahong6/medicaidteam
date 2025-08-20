from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os
import time

# Setup headless browser
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Load the page
url = "https://hfs.illinois.gov/medicalproviders/costreports/2023medicaidhospitalcaostreports.html"
driver.get(url)
time.sleep(3)  # Wait for JS to load

# Parse the rendered HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Find the container and extract links
pdf_container = soup.find(id='list-949c81eff0')
pdf_links = pdf_container.find_all('a', href=True) if pdf_container else []

# Create folder
os.makedirs('pdfs', exist_ok=True)

# Download PDFs
for link in pdf_links:
    href = link['href']
    if href.endswith('.pdf'):
        pdf_url = href if href.startswith('http') else f'https://hfs.illinois.gov{href}'
        pdf_name = pdf_url.split('/')[-1]

        print(f"Downloading {pdf_name}...")
        try:
            pdf_response = requests.get(pdf_url)
            with open(os.path.join('pdfs', pdf_name), 'wb') as f:
                f.write(pdf_response.content)
        except Exception as e:
            print(f"Failed to download {pdf_name}: {e}")
