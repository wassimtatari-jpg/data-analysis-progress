import pandas as pd

station_north = pd.DataFrame({
    "city": ["Tangier", "Tetouan", "Chefchaouen"],
    "station_id": [101, 102, 103],
    "pm25": [18, 22, 12],
    "temperature": [21, 19, 17]
})

station_south = pd.DataFrame({
    "city": ["Marrakech", "Agadir", "Essaouira"],
    "station_id": [201, 202, 203],
    "pm25": [35, 16, 11],
    "temperature": [29, 25, 23]
})

station_center = pd.DataFrame({
    "city": ["Casablanca", "Rabat", "Meknes"],
    "station_id": [301, 302, 303],
    "pm25": [28, 20, 24],
    "temperature": [26, 24, 22]
})
my_tables=pd.concat([station_north,station_south,station_center],axis=0,keys=(['north','south','center']))
print(my_tables)