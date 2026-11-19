import pandas as pd

products = pd.DataFrame({
    'product_id': [101, 102, 103, 104, 105],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Camera', 'Watch'],
    'price': [800, 400, 300, 500, 200]
})

sales = pd.DataFrame({
    'product_id': [102, 103, 104, 106],
    'price': [420, 280, 550, 700],
    'quantity': [5, 8, 3, 2]
})

new_table=products.merge(sales,on='product_id',how="inner",suffixes=('_product',"_sales"))
print(new_table)