# Write your MySQL query statement below
delete from Person
where (id,email) in (select T.id,T.email from (select * , (row_number() over(partition by email order by id) ) as rk from Person ) T 
where T.rk > 1
) ;
