import pandas as pd
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Ali', 'Omar', 'Sara', 'Lina', 'Adam']
})

orders = pd.DataFrame({
    'customer_id': [2, 3, 5, 6],
    'amount': [200, 350, 150, 400]
})
merge_table=customers.merge(orders,on='customer_id',how='inner')
print(merge_table)
