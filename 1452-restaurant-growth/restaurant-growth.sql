# Write your MySQL query statement below
WITH daily AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
rolling AS (
    SELECT
        visited_on,
        amount,
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS total_amount,
        COUNT(*) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS days
    FROM daily
)
SELECT
    visited_on,
    total_amount AS amount,
    ROUND(total_amount / days, 2) AS average_amount
FROM rolling
WHERE days = 7
ORDER BY visited_on;