Project Focus: Economic impacts of Medicaid spending in Illinois

Statement: This project aims to scrape a data table from the internet, which is focused on the economic impact of Medicaid reductions, specifically highlighting potential job losses. The outcome of this data analysis is a heatmap, which you can find here https://www.datawrapper.de/_/LUiem/

Tools and Libraries Used Python and Pandas

Dataset from the American Hospital Association. URL for original dataset - https://www.aha.org/fact-sheets/2025-06-05-medicaid-spending-reductions-would-lead-losses-jobs-economic-activity-and-tax-revenue-states

Methodology Download csv from coding script. Once downloaded, you can use the formula =REGEXEXTRACT(A1, "<td>(.+)</td>") in Google Sheets or Excel to make the file easier to analyze. After customizing it, you can download the sheet and upload the data to DataWrapper to create a choropleth map. Color by and label the map with job loss data across the nation--highlighting Illinois-specific data.
