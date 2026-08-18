# Write your MySQL query statement below
SELECT
    p.product_id,
    p.product_name
FROM Sales s
JOIN Product p
    ON p.product_id = s.product_id
WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
AND p.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
    )
GROUP BY p.product_id, p.product_name;