# Write your MySQL query statement below

select distinct(class) from Courses group by class having count(student) >= 5;