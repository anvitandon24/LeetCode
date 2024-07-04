import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, employee, left_one='managerId').
right_on='id', how='inner', suffixes= ('_e','_m'))
    return df [df['salary_e']>df ['salary_m']][['name_e]].rename
(columns={'name_e':'Employee'})