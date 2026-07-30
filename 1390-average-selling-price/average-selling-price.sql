select P.product_id , ifnull(round(sum(US.units*P.price)/sum(US.units),2),0) as average_price from Prices P 
left join UnitsSold  US 
on P.product_id = US.product_id and US.purchase_date between P.start_date and P.end_date

group by product_id 
order by product_id
;