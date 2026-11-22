import pandas as pd
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Ahmed', 'Sara', 'Omar', 'Lina', 'Youssef'],
    'city': ['Tangier', 'Rabat', 'Casa', 'Tangier', 'Fes']
})

orders = pd.DataFrame({
    'client_id': [1, 2, 2, 4, 6],
    'order_id': [101, 102, 103, 104, 105],
    'amount': [500, 300, 700, 250, 900]
})

payments = pd.DataFrame({
    'order_id': [101, 102, 104, 105, 106],
    'amount': [500, 300, 250, 900, 400],
    'payment_status': ['Paid', 'Paid', 'Pending', 'Paid', 'Failed']
})
customers_orders=customers.merge(orders,left_on='customer_id',right_on='client_id',how='outer')
print(customers_orders)

payments_merge=customers_orders.merge(payments,on='order_id',how="left",suffixes=('_order',"_payment"))
print(payments_merge)

payments_merge.describe()
print(payments_merge['payment_status'].isnull())
print(payments_merge.loc[payments_merge['payment_status'].isnull()])