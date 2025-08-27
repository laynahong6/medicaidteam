# Mapping Medicaid shortfalls in Illinois rural hospitals

This project identifies and maps rural hospitals in Illinois, and the level of Medicaid shortfalls they are facing. 

1. Find all the Illinois rural hospitals
Il_rural_hospital.py: Filtered Illinois rural hospitals
--> Il_rural _hospitals.csv

2. Download all Illinois rural hospital's 2023 cost report
medicaid_pdf_download.py: Use selenium and beautifulsoup to download PDF according to the hospital IDs
-->rural_hospital_costs_pdfs folder

3. Extract shortfall number 
medicaid_shortfall.py: locate the shortfall data, export shortfall, ID and page_info to csv
-->medicaid_shortfall.csv

4. Get geocode based on address
rural_hospital_geocode.py: use geocodio to get longitudes and latitudes
-->geocoded_rural_hospitals.csv: combine with all other hospital infomation
-->il_rural_hospitals_final.csv

5. Visualization
index.html: download Illinois counties.geojson and start building visualization using d3
