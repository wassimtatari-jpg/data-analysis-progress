
import pandas as pd

# Customers DataFrame
customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ahmed', 'Sara', 'Omar']
})

# Orders DataFrame
orders = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer_id': [1, 2, 3],
    'product_id': [201, 202, 203]
})

# Products DataFrame
products = pd.DataFrame({
    'product_id': [201, 202, 203],
    'product_name': ['Laptop', 'Phone', 'Tablet']
})

# Payments DataFrame
payments = pd.DataFrame({
    'order_id': [101, 102, 103],
    'payment_method': ['Card', 'Cash', 'Card']
})
merge_table1=orders.merge(customers,on="customer_id")
print(merge_table1)
merge_table2=merge_table1.merge(products,on='product_id')
print(merge_table2)
merge_table3=merge_table2.merge(payments,on="order_id")
print(merge_table3)
print(merge_table3.shape)
print(merge_table3.columns)