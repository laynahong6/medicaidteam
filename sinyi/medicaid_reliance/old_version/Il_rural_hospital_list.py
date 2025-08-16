import pandas as pd

#read the csv
df_rural_hospital = pd.read_csv('/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/rural_hospital_list.csv')
df_medicaid_hospital = pd.read_csv('/Users/asy/Documents/Medill MSJ/Github/Advanced Journalism/medicaidteam/sinyi/medicaid_hospital.csv')

#joining the csv
merge_df = pd.merge(
    left = df_rural_hospital,
    right = df_medicaid_hospital, 
    how = 'left',
    on= 'ID'
)

#save as csv
merge_df.to_csv('combined_rural_hospital_list.csv', index=False)
