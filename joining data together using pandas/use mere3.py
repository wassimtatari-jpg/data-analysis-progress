import pandas as pd

employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105],
    'name': ['Ali', 'Sami', 'Omar', 'Youssef', 'Karim'],
    'department': ['IT', 'HR', 'IT', 'Sales', 'HR']
})

salaries = pd.DataFrame({
    'emp_id': [102, 103, 104, 106],
    'salary': [5000, 7000, 6000, 8000]
})
table_mereg=employees.merge(salaries,on='emp_id',how="inner")
print(table_mereg)