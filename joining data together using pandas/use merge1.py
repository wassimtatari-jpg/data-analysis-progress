import pandas as pd

taxi_owners = pd.DataFrame({
    'vid': [101, 102, 103, 104],
    'owner': ['Ahmed', 'Sami', 'Omar', 'Karim']
})

taxi_veh = pd.DataFrame({
    'vid': [101, 102, 103, 105],
    'model': ['Toyota', 'Dacia', 'Hyundai', 'Renault']
})
#use merge
merge_table=taxi_owners.merge(taxi_veh,on="vid",how='inner')
print(merge_table)