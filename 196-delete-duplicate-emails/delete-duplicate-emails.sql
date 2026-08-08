# Write your MySQL query statement belowdele
delete from Person 
where id in ( select id from 
    (select * , row_number() over(partition by email order by id ) as rk from Person ) P 
    where P.rk > 1 
    );
    
    