import pandas as pd
researchers = pd.DataFrame({
    "researcher_id": [201, 202, 203, 204, 205, 206],
    "researcher_name": [
        "Adam", "Sarah", "John", "Maya", "David", "Lina"
    ],
    "country": [
        "Morocco", "Kenya", "Egypt", "Morocco", "Kenya", "Egypt"
    ]
})

field_reports = pd.DataFrame({
    "report_id": [1, 2, 3, 4, 5],
    "researcher_id": [201, 203, 201, 206, 209],
    "reports_count": [5, 3, 2, 4, 1]
})
#Semi Join
reseacher_have_report=researchers[researchers['researcher_id'].isin(field_reports['researcher_id'])]
print(reseacher_have_report)
