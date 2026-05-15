# Real-Time Market Analytics Dashboard

A data science project that implements a complete ETL pipeline to visualize Bitcoin market trends and generate algorithmic trading signals.

## Features
- **Data Extraction:** Automated retrieval of 1-hour interval market data via Yahoo Finance API.
- **Data Processing:** Vectorized calculations using pandas to generate 24h Simple Moving Averages (SMA).
- **Algorithmic Signals:** Automated logic to generate Buy/Sell indicators based on price-to-SMA crossovers.
- **Visualization:** Interactive dashboard showing price fluctuations, trading volume, and signal distribution.

## Tech Stack
- **Language:** Python 3.12 (ARM64 version)
- **Libraries:** pandas, yfinance
- **BI Tool:** Power BI 

## Dashboard Preview
![Dashboard Preview](dashboard.pbix)

## How it works
The `main.py` script fetches real-time data, processes technical indicators, and exports a clean CSV. This structured data is then mapped into a Power BI model for business intelligence reporting.
