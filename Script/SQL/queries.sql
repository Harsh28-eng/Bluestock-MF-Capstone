-- Top 5 Funds by AUM
SELECT * FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Total Transactions
SELECT COUNT(*)
FROM fact_transactions;

-- Average AUM
SELECT AVG(aum)
FROM fact_aum;

-- Max NAV
SELECT MAX(nav)
FROM fact_nav;

-- Min NAV
SELECT MIN(nav)
FROM fact_nav;

-- Fund Count by Category
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- Top 5 Returns
SELECT *
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;