import pandas as pd
employees = pd.DataFrame({
    "employee_id": [301, 302, 303, 304],
    "name": ["Wassim", "Salem", "Ahmad", "Khaled"]
})
branches = pd.DataFrame({
    "branch_id": [10, 20, 30],
    "branch_name": ["Tangier", "Rabat", "Casablanca"]
})
work_records = pd.DataFrame({
    "employee_id": [301, 301, 302, 303, 304, 304],
    "branch_id": [10, 10, 20, 30, 30, 30],
    "hours": [8, 7, 8, 6, 8, 7]
})
new_employees = pd.DataFrame({
    "employee_id": [305, 306, 301],
    "name": ["Omar", "Hassan", "Ali"]
})
employee_report=employees.merge(work_records,on="employee_id",how="inner",validate="one_to_many")
print(employee_report)

whole_employ=pd.concat([employees,new_employees],ignore_index=True,verify_integrity=True)
chek_emp=whole_employ[whole_employ['employee_id'].duplicated(keep=False)]
print(chek_emp)