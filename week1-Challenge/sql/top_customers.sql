-- The highest-ranked countries generate the most revenue.
SELECT Customer.CustomerId, Customer.FirstName || ' ' || Customer.LastName AS CustomerName, 
SUM(Invoice.Total) AS TotalSpend
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpend DESC
LIMIT 5;