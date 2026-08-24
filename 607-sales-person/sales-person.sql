# Write your MySQL query statement below
SELECT sp.name
FROM SalesPerson sp
LEFT JOIN (
    SELECT DISTINCT o.sales_id
    FROM Orders o
    JOIN Company c
        ON o.com_id = c.com_id
    WHERE c.name = 'RED'
) red_sales
    ON sp.sales_id = red_sales.sales_id
WHERE red_sales.sales_id IS NULL;