import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "product": ["Laptop", "Phone", "Laptop", "Phone", "Laptop"],
    "order_time": pd.to_datetime([
        "2026-01-01 10:05",
        "2026-01-01 10:12",
        "2026-01-01 10:25",
        "2026-01-01 10:40",
        "2026-01-01 11:10"
    ])
})
prices = pd.DataFrame({
    "product": ["Laptop", "Phone", "Laptop", "Phone",
                "Laptop", "Phone"],
    "price_time": pd.to_datetime([
        "2026-01-01 09:00",
        "2026-01-01 09:30",
        "2026-01-01 10:20",
        "2026-01-01 10:35",
        "2026-01-01 11:00",
        "2026-01-01 11:05"
    ]),
    "price": [900, 500, 950, 520, 980, 540]
})
orders=orders.sort_values(by="order_time")
prices=prices.sort_values(by="price_time")
merge_table=pd.merge_asof(orders,prices,by="product",left_on='order_time',right_on="price_time",direction="backward",tolerance=pd.Timedelta("15min"))
print(merge_table)