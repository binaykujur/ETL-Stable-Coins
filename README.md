# 🪙 **Stablecoin Intelligence: From API Extraction To SQL Analysis**

This project focuses on **analyzing stablecoins** using a dataset containing various financial metrics. The analysis is performed using **SQL Server** and **Python (Pandas and Matplotlib/Seaborn for visualization)** to gain insights into market behavior, liquidity, volatility, and potential anomalies.

---

## 📁 **Table of Contents**
1. [Project Overview](#project-overview)  
2. [Dataset Description](#dataset-description)  
3. [Technologies Used](#technologies-used)  
4. [Key Analysis and Insights](#key-analysis-and-insights)  
5. [SQL Scripts](#sql-scripts)  
6. [Python Scripts](#python-scripts)  
7. [Results](#results)  
8. [How to Run the Project](#how-to-run-the-project)  
9. [Contributing](#contributing)  
10. [License](#license)  

---

## 📌 **1. Project Overview**
The goal of this project is to:
- Perform **data cleaning and feature engineering** using **Python (Pandas)**.  
- Execute **advanced SQL queries** in **SQL Server** to analyze market cap, volume, price movements, and liquidity.  
- Visualize the results to detect **anomalies, trends, and outliers** in the stablecoins market.  

---

## 🗂 **2. Dataset Description**
**Filename:** `stablecoins_data.csv`  
**Columns:**
- `id`  
- `symbol`  
- `name`  
- `current_price_usd`  
- `market_cap_usd`  
- `total_volume_usd`  
- `high_24h_usd`  
- `low_24h_usd`  
- `price_change_24h`  
- `price_volatility_24h`  
- `market_cap_to_volume_ratio`  
- `normalized_price`  
- `price_movement_category`  
- `log_market_cap_usd`  
- `log_total_volume_usd`  
- `hour_of_day`  
- `day_of_week`  
- `last_updated`  

**Total Records:**  100
**Source:** [coingecko](https://api.coingecko.com/api/v3/coins/markets)  

---

## ⚙️ **3. Technologies Used**
- **Programming Languages:** Python, SQL  
- **Database:** SQL Server  
- **Libraries:**  
  - **Python:** Pandas, Matplotlib, Seaborn, NumPy  
  - **SQL:** Window functions, CTEs, and statistical functions  

---

## 🔍 **4. Key Analysis and Insights**
1. **Summary Statistics:** Calculated mean, max, min, and standard deviation for prices and volumes.  
2. **Market Cap Analysis:** Identified top stablecoins by market cap.  
3. **Price Movement:** Analyzed price categories and volatility.  
4. **Liquidity Analysis:** Evaluated market cap to volume ratio.  
5. **Anomaly Detection:** Used **Z-Scores** to spot outliers.  
6. **Time-Series Analysis:** Assessed average price trends by day and hour.  
7. **Correlation Analysis:** Examined relationships between market cap and volume.  

---

## 🛠 **5. SQL Scripts**
**Key SQL Queries:**
- **Summary Statistics:**  
  ```sql
  SELECT AVG(current_price_usd), MAX(current_price_usd), MIN(current_price_usd) FROM stablecoins;
- **Top 5 Stable Coins by market cap**
    ```sql
    SELECT TOP 5 name, market_cap_usd FROM stablecoins ORDER BY market_cap_usd DESC;
- **Detecting Anamolies**
    ```sql
    WITH ratio_stats AS (
    SELECT AVG(market_cap_to_volume_ratio) AS avg_ratio, STDEV(market_cap_to_volume_ratio) AS stddev_ratio
    FROM stablecoins_data
    )
    SELECT name, symbol FROM stablecoins_data, ratio_stats
    WHERE ABS((market_cap_to_volume_ratio - avg_ratio) / stddev_ratio) > 2;




## 🐍 **6. Python Scripts**
**Key Python Files:**

- extraction.py: Extracts the data from the coingecko API
- cleaning_extraction.py: performs data cleaning and feature engineering using pandas

**Location:** scripts/

## 📊 **7. Results**
- Market Cap vs. Volume: Found a strong positive correlation indicating a healthy market.
- Outliers: Detected stablecoins with unusually high market cap-to-volume ratios.
- Volatility: Identified assets with high 24-hour volatility for potential high-risk investments.
- Active Trading Hours: Most trades occurred between 12 PM to 4 PM UTC.