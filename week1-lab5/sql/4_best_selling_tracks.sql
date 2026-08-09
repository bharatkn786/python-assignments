-- Shows the 10 best-selling tracks.

SELECT Track.TrackId, Track.Name, SUM(InvoiceLine.Quantity) AS Quantity
FROM InvoiceLine
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.TrackId, Track.Name
ORDER BY Quantity DESC
LIMIT 10;
