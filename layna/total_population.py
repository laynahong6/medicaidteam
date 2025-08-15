import pandas as pd
import requests, json
from bs4 import BeautifulSoup
import csv

df = pd.read_csv ('censusdata_ALL.csv')