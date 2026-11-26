import pandas as pd

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105, 106],
    "name": ["Ahmad", "Sara", "Omar", "Lina", "Khaled", "Maya"],
    "city": ["Tangier", "Rabat", "Casablanca", "Tangier", "Rabat", "Fes"]
})

orders = pd.DataFrame({
    "order_id": [5001, 5002, 5003, 5004, 5005],
    "customer_id": [102, 104, 102, 106, 103],
    "amount": [250, 400, 150, 600, 300]
})
my_table=customers.merge(orders,how='inner',on="customer_id")
new=my_table.drop_duplicates(subset="customer_id")
print(new['name'])

order_customer_id=orders.drop_duplicates(subset="customer_id")
print(order_customer_id['customer_id'])

special_customers=customers[customers["customer_id"].isin(order_customer_id['customer_id'])]
print(special_customers)

customers_no_order=customers[~customers["customer_id"].isin(order_customer_id['customer_id'])]
print(customers_no_order)
customers_from_tangier=customers[(customers["customer_id"].isin(order_customer_id["customer_id"]))&(customers["city"]=="Tangier")]
print(customers_from_tangier)