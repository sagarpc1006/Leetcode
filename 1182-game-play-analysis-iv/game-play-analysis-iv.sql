# Write your MySQL query stateme
SELECT 
    ROUND(
        SUM(CASE WHEN DATEDIFF(event_date, first_date) = 1 THEN 1 ELSE 0 END) 
        / COUNT(DISTINCT player_id), 
    2) AS fraction
FROM (
    SELECT 
        player_id, 
        event_date,
        MIN(event_date) OVER (PARTITION BY player_id) AS first_date
    FROM Activity
) AS T;