# Write your MySQL query statement below
select query_name ,round(avg(rating/position),2) as quality 
,  round((select count(rating) from Queries Q2 where Q2.rating <3 and Q2.query_name=Q1.query_name)*100/(count(rating)),2) as poor_query_percentage
from Queries Q1
group by query_name ;
