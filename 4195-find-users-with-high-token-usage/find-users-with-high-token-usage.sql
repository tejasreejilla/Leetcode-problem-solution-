# Write your MySQL query statement below
SELECT
    p.user_id,
    COUNT(*) AS prompt_count,
    ROUND(AVG(p.tokens), 2) AS avg_tokens
FROM prompts p
GROUP BY p.user_id
HAVING COUNT(*) >= 3
   AND EXISTS (
       SELECT 1
       FROM prompts p2
       WHERE p2.user_id = p.user_id
         AND p2.tokens > AVG(p.tokens)
   )
ORDER BY avg_tokens DESC, p.user_id ASC;