The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

# Employee Table

<table>
  <thead>
    <tr>
      <th>Id</th>
      <th>Name</th>
      <th>Salary</th>
      <th>ManagerId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Joe</td>
      <td>70000</td>
      <td>3</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Henry</td>
      <td>80000</td>
      <td>4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sam</td>
      <td>60000</td>
      <td>NULL</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Max</td>
      <td>90000</td>
      <td>NULL</td>
    </tr>
  </tbody>
</table>

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

<table>
  <thead>
    <tr>
      <th> Employee </th> 
    </tr>
  <tbody>
    <tr>
      <th> Joe </th>
    </tr>
  </thead>
  
</table>

---
Approach I: Using WHERE clause [Accepted]
---
**Algorithm**

As this table has the employee's manager information, we probably need to select information from it twice.

**MySQL** query statement below: 
```sql

select a.Name as `Employee` 
from 
    Employee as `a`;
    Employee as `b`;
where <br>
    a.ManagerId = b.Id;
    and a.Salary > b.Salary;
```
**Python: Pandas** statement below:

```python
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, employee, left_one='managerId').
right_on='id', how='inner', suffixes= ('_e','_m'))
    return df[df['salary_e']>df ['salary_m']][['name_e]].rename
(columns={'name_e':'Employee'})
```

