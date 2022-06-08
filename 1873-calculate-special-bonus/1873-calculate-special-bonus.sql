/* Write your PL/SQL query statement below */
select employee_id, 
CASE WHEN employee_id % 2 = 0 THEN 0
    WHEN name like 'M%' THEN 0
    ELSE salary END
as bonus
from Employees;
    