# Write your MySQL query statement below

WITH cte AS (
    SELECT 
        *,
        SUM(weight) OVER(ORDER BY Turn) AS total_weight
    FROM Queue 
) 

SELECT person_name FROM cte 
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
    