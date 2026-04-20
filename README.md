# COVID-19 Global Data Analysis 🌍

## Overview
This project provides a deep-dive analysis of the COVID-19 pandemic, processing over 300,000 records across 200+ countries. Using a combination of Python for data engineering, SQL for complex analytical querying, and Tableau for interactive storytelling, I've mapped out the relationship between vaccination rates, infection surges, and mortality outcomes.

## Live Dashboard


---

## 🛠️ Tools & Technologies
* **Python (Pandas/NumPy):** Data cleaning, handling missing values, and feature engineering.
* **MySQL:** Advanced SQL analysis using Window Functions (rolling averages) and CTEs.
* **Tableau:** Interactive data visualization, dual-axis charts, and geographic mapping.

## 📈 Key Analysis & Skills Demonstrated
* **Data Cleaning:** Automated the filtering of non-country entities (continents/income groups) and handled missing values across 60+ columns.
* **Advanced SQL:** * Used **Window Functions** (`PARTITION BY`) to calculate 7-day rolling averages of new cases.
    * Implemented **CTEs** (Common Table Expressions) to correlate vaccination coverage with death rates.
* **Tableau Dashboarding:** * **World Heatmap:** Visualized global cases per million.
    * **Scatter Plot Analysis:** Identified the correlation between full vaccination status and mortality rates.
    * **Dual-Axis Trends:** Compared monthly case surges vs. death trends on a unified timeline.

## 📁 Project Structure
* `clean_covid.py`: Python script for preprocessing raw data.
* `analysis_covid.sql`: SQL script containing the analytical queries used for the report.
* `README.md`: Project documentation and findings.

## 📊 Data Source
The data is sourced from **Our World in Data**. 
> **Note:** The raw dataset is ~150MB and is not uploaded to this repository. You can download the latest version here: [Our World in Data COVID Dataset](https://github.com/owid/covid-19-data/tree/master/public/data)

## 💡 Key Findings

---