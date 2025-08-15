import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

#build useragent
geolocator = Nominatim (user_agent='IllinoisHospital_MedicaidCut (github.com/sinyiau)')
                
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.1, error_wait_seconds=10.0)

#read csv
df = pd.read_csv('/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/rural_hospital_address.csv')

#get latitude and longitude
df['Latitude'] = None
df['Longitude'] = None

start_time = time.time()





