-- Shows revenue for each month in 2010.
SELECT strftime('%m', InvoiceDate) AS Month,
       SUM(Total) AS Revenue
FROM Invoice
WHERE InvoiceDate LIKE '2010%'
GROUP BY Month;
