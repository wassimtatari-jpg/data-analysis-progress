import pandas as pd

employees = pd.DataFrame({
    'emp_id': [101, 102, 103],
    'name': ['Ali', 'Sami', 'Omar'],
    'department': ['IT', 'HR', 'Sales']
})

performance = pd.DataFrame({
    'emp_id': [101, 102, 103],
    'name': ['Ali A', 'Sami B', 'Omar C'],
    'rating': [4, 5, 3]
})
merge_table_suffiex=employees.merge(performance,on='emp_id',how="inner",suffixes=("_emp","_perf"))
print(merge_table_suffiex)