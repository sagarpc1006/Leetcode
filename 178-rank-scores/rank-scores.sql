# Write your MySQL query statement below
select T.score , T.rk as "rank" from
(select * , dense_rank() over(order by score desc) as rk from Scores) as T
order by T.score desc , T.rk asc ;