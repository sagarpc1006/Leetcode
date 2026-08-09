# Write your MySQL query statement below
select P.product_name as product_name , sum(O.unit) as unit from Orders O 
left join Products P 
on O.product_id = P.product_id 
where (year(O.order_date) = '2020' and month(O.order_date) ='02')
group by P.product_name 
having sum(O.unit) >= 100 ;