import pandas as pd

registered_stations = pd.DataFrame({
    "station_id": [101, 102, 103, 104, 105, 106, 107],
    "city": ["Tangier", "Tetouan", "Rabat", "Casablanca",
             "Marrakech", "Agadir", "Chefchaouen"],
    "region": ["North", "North", "Center", "Center",
               "South", "South", "North"]
})

readings_north = pd.DataFrame({
    "reading_id": [1, 2, 3, 4],
    "station_id": [101, 102, 108, 101],
    "pm25": [18, 22, 30, 20],
    "temperature": [21, 19, 24, 22]
})

readings_south = pd.DataFrame({
    "reading_id": [5, 6, 7, 8],
    "station_id": [105, 106, 109, 103],
    "pm25": [35, 16, 28, 25],
    "temperature": [29, 25, 27, 24]
})

readings_center = pd.DataFrame({
    "reading_id": [9, 10, 11, 12],
    "station_id": [103, 104, 110, 107],
    "pm25": [23, 28, 32, 12],
    "temperature": [23, 26, 28, 17]
})
all_readings_table=pd.concat([readings_north,readings_south,readings_center],keys=(['north',"south",'center']))
print(all_readings_table)

registered_stations_readings=registered_stations[registered_stations["station_id"].isin(all_readings_table['station_id'])]
print(registered_stations_readings)

stations_readings_no_rgistered=all_readings_table[~all_readings_table['station_id'].isin(registered_stations["station_id"])]
print(stations_readings_no_rgistered)

north_readings_registered1=registered_stations[(registered_stations["station_id"].isin(all_readings_table['station_id']))&(registered_stations["region"] == "North")]
print(north_readings_registered1)


north_readings_registered=readings_north[readings_north["station_id"].isin(registered_stations["station_id"])]
print(north_readings_registered)
south_readings_registered=readings_south[readings_south["station_id"].isin(registered_stations["station_id"])]
print(south_readings_registered)
center_readings_registered=readings_center[readings_center["station_id"].isin(registered_stations['station_id'])]
print(center_readings_registered)
final_table=pd.concat([north_readings_registered,south_readings_registered,center_readings_registered],keys=['north','south','centre'])
print(final_table)