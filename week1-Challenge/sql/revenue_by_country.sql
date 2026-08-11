-- Shows total revenue for each country.

SELECT Country, SUM(Total) AS Revenue
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Country
ORDER BY Revenue DESC;