import requests
from bs4 import BeautifulSoup

#Step 1: Fetch the webpate
url = "https://hfs.illinois.gov/medicalproviders/costreports/2023medicaidhospitalcaostreports.html"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

#Step 2: Find the container with the PDFs
pdf_container = soup.find(id='list-949c81eff0')
print("Container found:", bool(pdf_container))

#Step 3: Find all the links
if pdf_container:
    pdf_links = pdf_container.find_all('a',href=True)

    for link in pdf_links:
        href = link['href']
        if href.endswith('.pdf'):
            pdf_url = href if href.startswith('http') else f'https://hfs.illinois.gov{href}'
            pdf_name = pdf_url.split('/')[-1]

            pdf_response = requests.get(pdf_url)
            with open(pdf_name, 'wb') as f:
                f.write(pdf_response.content)