import pandas as pd

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "customer_name": ["Wassim", "Mohamed", "Salem", "Ali"]
})
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer_id": [101, 101, 102, 103, 103, 104],
    "amount": [200, 350, 150, 400, 250, 100]
})
new_customers = pd.DataFrame({
    "customer_id": [105, 106, 101],
    "customer_name": ["Ahmad", "Khaled", "Omar"]
})
my_table=customers.merge(orders,on="customer_id",how="inner",validate="one_to_many")
print(my_table)
check=customers[customers['customer_id'].duplicated()]
print(check)
new_customers_table=pd.concat([customers,new_customers],ignore_index=True,verify_integrity=True)
print(new_customers_table)
sorte_table=new_customers_table[new_customers_table['customer_id'].duplicated(keep=False)]
print(sorte_table)