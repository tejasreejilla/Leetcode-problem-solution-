# Write your MySQL query statement below
WITH friends AS (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
),
friend_count AS (
    SELECT id, COUNT(*) AS num
    FROM friends
    GROUP BY id
),
ranked AS (
    SELECT id, num,
           DENSE_RANK() OVER (ORDER BY num DESC) AS rnk
    FROM friend_count
)
SELECT id, num
FROM ranked
WHERE rnk = 1;