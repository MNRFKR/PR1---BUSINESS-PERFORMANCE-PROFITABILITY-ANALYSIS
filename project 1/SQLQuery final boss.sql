SELECT 
    Category,
    SUM(CAST([Units Sold] AS INT)) AS TotalUnits,
    AVG(CAST(Discount AS FLOAT)) AS AvgDiscount,
    SUM(CAST([Units Sold] AS INT) * CAST(Price AS FLOAT)) AS Revenue
FROM [RAW SALES DATA]
GROUP BY Category;
SELECT DISTINCT [Units Sold] FROM [RAW SALES DATA];
SELECT DISTINCT Price FROM [RAW SALES DATA];
SELECT DISTINCT Discount FROM [RAW SALES DATA];
SELECT Category, SUM([Units Sold] * CAST(Price AS FLOAT)) AS Revenue
FROM [RAW SALES DATA]
GROUP BY Category
ORDER BY Revenue DESC;
SELECT Category, AVG(CAST(Discount AS FLOAT)) AS AvgDiscount
FROM [RAW SALES DATA]
GROUP BY Category;
