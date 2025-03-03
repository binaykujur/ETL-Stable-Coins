-- stablecoins dataset we are working on
SELECT * FROM stablecoins;

-- 1 Basics summary Statistics
-- Purpose: Get an overview of key statistics like count, average, min, max, and standard deviation for important columns
SELECT 
    COUNT(*) AS total_records,
    AVG(current_price_usd) AS avg_price,
    MIN(current_price_usd) AS min_price,
    MAX(current_price_usd) AS max_price,
    STDEV(current_price_usd) AS stddev_price,
    AVG(market_cap_usd) AS avg_market_cap,
    AVG(total_volume_usd) AS avg_total_volume
FROM stablecoins;
--Insights: Understand central tendency and spread for prices, market cap, and volume.
---------------------------------------------------------------------------------------------------

-- 2. Top 5 Stablecoins by Market Cap
-- Purpose: Identify the most valuable assets based on market cap.

SELECT TOP 5
    name,
    symbol,
    market_cap_usd
FROM stablecoins
ORDER BY market_cap_usd DESC;
-----------------------------------------------------------------------------------------------------

-- 3. Price movement analysis
-- Purpose: Categorize assets based on price movement.
SELECT 
    price_movement_category,
    COUNT(*) AS count_assets
FROM stablecoins
GROUP BY price_movement_category;
-- Insight: Understand the market sentiment (upward, downward, stable).
-------------------------------------------------------------------------------------------------------

-- 4. Average Price by Price movement category
-- purpose: Compare average prices across different price movement categories.
SELECT 
    price_movement_category,
    AVG(current_price_usd) AS avg_price
FROM stablecoins
GROUP BY price_movement_category
ORDER BY avg_price DESC;
---------------------------------------------------------------------------------------------------------


-- 5. Detecting Anomalous Price Changes
-- Purpose: Identify assets with unusually high price changes in 24 hours.

SELECT 
    name,
    symbol,
    current_price_usd,
    price_change_24h
FROM stablecoins
WHERE ABS(price_change_24h) > 0.2  -- Change threshold as needed
ORDER BY price_change_24h DESC;

-- Insight: Spot potential outliers or manipulated prices
-------------------------------------------------------------------------------------------------------------

-- 6.Liquidity Analysis: Market cap to Volume ratio
-- Purpose: Identify liquid vs. illiquid assets.

SELECT 
    name,
    symbol,
    market_cap_to_volume_ratio
FROM stablecoins
WHERE market_cap_to_volume_ratio > 10
ORDER BY market_cap_to_volume_ratio DESC;
-- Insight: High ratios suggest low liquidity
-----------------------------------------------------------------------------------------------------------

-- 7. Price Volatality Analysis
-- purpose: Identify assets with high price volatality
SELECT 
    name,
    symbol,
    price_volatility_24h
FROM stablecoins
WHERE price_volatility_24h > (
    SELECT AVG(price_volatility_24h) * 2 FROM stablecoins
)
ORDER BY price_volatility_24h DESC;
-- Insight: Spot high-risk, high-reward assets.
-------------------------------------------------------------------------------------------------------------








