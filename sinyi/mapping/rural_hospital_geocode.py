import pandas as pd
from geocodio import Geocodio
import time

#Build clean address from Il hospital list
hospital_df = pd.read_csv("/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/Il_rural_hospitals.csv")

hospital_df["Address"] = (
    hospital_df["ADDRESS"].astype(str).str.strip() + ", " +
    hospital_df["CITY"].astype(str).str.strip() + ", " +
    hospital_df["STATE"].astype(str).str.strip() + ", " +
    hospital_df["ZIP"].astype(str).str.strip() 
)

hospital_df[["Address"]].to_csv("rural_hospital_address.csv",index=False)

#Get long&lat with Geocodio
client = Geocodio("68cdb0f2ba99e5bab6eb2e5ecb288e19ecdc5a6")

address_path = "rural_hospital_address.csv"

with open(address_path, "rb") as f:
    new_list = client.create_list(
        file = f,
        filename = "rural_hospital_address.csv",
        direction = "forward"
    )

while True:
    list_details = client.get_list(new_list.id)
    state = list_details.status.get("state")
    if state == "COMPLETED":
        break
    elif state == "FAILED":
        raise Exception("Geocoding failed")
    time.sleep(10)  

#Download geocoded results
client.download(new_list.id, "geocoded_rural_hospitals.csv")

#Merge geocoded results to hospital data
geo_df = pd.read_csv("geocoded_rural_hospitals.csv")
merged_df = hospital_df.merge(geo_df, on="Address", how="left")

#Merge Medicaid shortfall
shortfall_df = pd.read_csv("/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/medicaid_reliance/medicaid_shortfall.csv")
merged_df = merged_df.merge(shortfall_df, on="ID", how="left")

final_cols = [
    "ID", "NAME", "ADDRESS", "CITY", "STATE", "ZIP","Geocodio Latitude", "Geocodio Longitude", "Medicaid shortfall", "PHONE"
]
merged_df[final_cols].to_csv("Il_rural_hospitals_final.csv", index=False)

