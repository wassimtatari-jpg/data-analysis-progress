import pandas as pd

employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ahmed', 'Sami', 'Omar', 'Youssef', 'Ali', 'Karim'],
    'manager_id': [None, 1, 1, 2, 2, 3],
    'department': ['IT', 'IT', 'Sales', 'IT', 'Sales', 'Sales']
})
new_table=employees.merge(employees,left_on='manager_id',right_on='employee_id',suffixes=("_employee","_manager"))
print(new_table)