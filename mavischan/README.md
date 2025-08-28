READ ME: analysis of dual eligible enrollment in IL in July 2025
Languages used: R and Python 

Sources:
MMAI and HealthChoice IL enrollment by county: https://hfs.illinois.gov/content/dam/soi/en/web/hfs/sitecollectiondocuments/202507mcoaer.pdf
County population 2020: https://dph.illinois.gov/data-statistics/vital-statistics/illinois-population-data.html
Urban vs rural IL counties definition: https://dph.illinois.gov/content/dam/soi/en/web/idph/files/rur-urb-2021.pdf

Methodolody:
Acqusition and data cleaning:
Use tabula.py to extract tables from source pdf.
Export csv to R for further analysis and visualization.
Unify name spellings for enrollment data and county population data. 
Clean null values. 
Add code for each county on both datasets.
Inner join two datasets by county code column. 

Main focus of analysis:
Find out proportion of population on both Medicaid and Medicare (MMAI). Sort by highest to lowest.
Find out median rates for overall state, urban and rural counties.
Compare dual enrollment rates between rural and urban.
Bar graph focuses on urban-rural breakdown of counties with above median dual enrollment rates. 

Notes/caveat:
Some counties' MMAI enrollment numbers are masked (null) in source dataset because they "indicate at least one but fewer than six enrollees in the county to assure confidenality."
Those counties' numbers are replaced with '1' as a conservative estimate in order to calculate county/insurance type totals. 
Population data is taken from 2020 Census data, the most recent stastitics. 
