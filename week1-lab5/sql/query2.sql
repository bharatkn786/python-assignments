-- This query identifies the 10 tracks with the highest unit price.

SELECT *
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;
