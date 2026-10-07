#select max(salary) as SecondHighestSalary from Employee where ((salary) < (select max(salary) from Employee ))

# Below approach is almost right but not giving null values 
#select T.salary as SecondHighestSalary from ( select * ,rank() over(order by salary desc) as R from Employee ) as T where T.R=2;

# Most better approach 
select (
select distinct(salary) from Employee 
order by salary desc 
limit 1 OFFSET 1 
) as SecondHighestSalary 