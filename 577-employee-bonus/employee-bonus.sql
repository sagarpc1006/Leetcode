# Write your MySQL query statement below
select E.name , B.bonus from Employee E 
left join Bonus B 
on E.empID=B.empID 
where (B.bonus < 1000 or B.bonus is null );