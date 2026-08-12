select visited_on, amount, round(amount/7, 2) as average_amount
from (
    select visited_on,
           sum(amount) over (order by visited_on rows between 6 preceding and current row) as amount,
           row_number() over (order by visited_on) as rn
    from (select visited_on, sum(amount) as amount from Customer group by visited_on) as daily
) as t
where rn >= 7
order by visited_on;