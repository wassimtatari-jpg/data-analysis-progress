
import pandas as pd

properties = pd.DataFrame({
    'district': ['North', 'South', 'East', 'West'],
    'area': [120, 150, 100, 180],
    'property_type': ['Villa', 'Apartment', 'Villa', 'Apartment']
})

population = pd.DataFrame({
    'district': ['North', 'South', 'East', 'West'],
    'population': [50000, 75000, 40000, 60000],
    'density': [1200, 1800, 900, 1400]
})

sales = pd.DataFrame({
    'district': ['North', 'South', 'East', 'West'],
    'area': [120, 150, 100, 180],
    'sales_count': [35, 50, 25, 40]
})
merge_table=properties.merge(population,on='district')\
                       .merge(sales,on="district",suffixes=('_prop',"_sales"))
print(merge_table)