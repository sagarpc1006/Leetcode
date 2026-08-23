# Write your MySQL query statement below
select T.Department,T.Employee ,T.Salary from 
(select D.name as Department ,E.name as Employee ,E.salary as Salary , dense_rank() over(partition by D.name  order by E.salary desc ) as rk 
from Department D inner join Employee E 
on D.id = E.departmentId
) as T 
where rk < 4;