# Write your MySQL query statement below
select D.name as Department , E.name as Employee , E.salary as Salary 
from Employee E 
join Department D 
on E.departmentId = D.id 
where salary = (select max(salary) from Employee where departmentId  = E.departmentId );