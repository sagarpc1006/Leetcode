# Write your MySQL query statement below
select T.player_id , T.event_date as first_login from 
( select * , row_number() over(partition by player_id order by event_date asc) as rk  from Activity )
as T 
where T.rk = 1 ;
