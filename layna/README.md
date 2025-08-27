# Mapping Illinois county dependency on state health benefits (2024)

## Project statement

This end goal of this project is to create a joined dataset that can be used to make a visualization that shows the percentage of people enrolled in Illinois Healthcare and Family Services (HFS) by county. 

## Getting Started 

### Tools Used 
<b>Program</b>: Python

<b>Libraries</b>: requests, csv, json, pandas, bs4

## Data Sources 

<a href="https://www.census.gov/data/tables/time-series/demo/popest/2020s-counties-total.html">Annual Estimates of the Resident Population for Counties: April 1, 2020 to July 1, 2024</a> from U.S. Census Bureau 

<a href="https://hfs.illinois.gov/info/factsfigures/program-enrollment/countieslist.html">Number of clients enrolled in HFS program</a> from Illinois Department of Healthcare and Family Services

## Scripts 

### Web scraping HFS program enrollment data 

Script used: total_enrollment.py 

This script scrapes data from <a href="https://hfs.illinois.gov/info/factsfigures/program-enrollment/countieslist.html">this page</a>, going into each individual Illinois county webpage and retrieving the last table, which contains data on the total enrollment in HFS programs from 2020-24. 

After writing each data row, the script will sort the rows alphabetically by the first column, which contains the county names. The county names were retrieved from the end of each web url. 

### Illinois county population estimates

Script used: total_population.py 

This script cleans data from the U.S. Census to only include Illinois counties and the population estimates from 2020-2024. Then, the column containing each county name is changed to be lowercase with no commas, spaces or periods. This way, it will match the first column for the csv created from the total_enrollment.py script. 

### Joining datasets 

Script used: joined_database.py 

After creating county_enrollment.csv and county_population.csv, this script will join the datasets and include a new column that calculates the enrollment percentage for each county. 

## End Product 

At the end, you should get a .csv file that has four columns: 

<li>County Name</li>
<li>2024 Enrollment</li>
<li>2024 Population Estimate</li>
<li>Percentage</li>

Notes: These scripts can be changed to calculate percentage for different years, or even create datasets that show change over time. 

## Visualization

Files needed: Illinois_Counties.geojson, joined_output.csv 

A heat map showing the percentage of Illinoisians enrolled in state HFS can be created using shelf-ready tools, like Flourish. 

Example visualization created from this project <a href="https://public.flourish.studio/visualisation/24690537/">here</a>.




