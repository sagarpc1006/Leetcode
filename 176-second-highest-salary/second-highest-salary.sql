select max(salary) as SecondHighestSalary from Employee
where ((salary) < (select max(salary) from Employee ));
#select T.salary as SecondHighestSalary from ( select * ,rank() over(order by salary desc) as R from Employee ) as T where T.R=2;
