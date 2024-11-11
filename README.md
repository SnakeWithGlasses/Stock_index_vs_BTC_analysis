README.txt

Investment Performance Comparison using Python
==============================================

Overview
--------
This Python script enables users to analyze and compare the historical performance of various financial products, such as Bitcoin (BTC) and ETFs like SPY (S&P 500), URTH (MSCI World), and QQQ (Nasdaq 100). By visualizing normalized performance data, users can identify trends and make better investment decisions.

Features
--------
- **Data Collection**: Fetches historical data from Yahoo Finance using the `yfinance` library.
- **Data Normalization**: Standardizes data so that all assets start at the same base value, allowing for easy comparison.
- **Interactive Visualization**: Creates interactive line charts using `plotly` for comprehensive performance analysis.
- **Multiple Comparisons**:
  - A chart comparing SPY, BTC, URTH, and QQQ.
  - A chart comparing only SPY, URTH, and QQQ.

Requirements
------------
- Python 3.x
- Libraries: `yfinance`, `pandas`, `plotly`

Installation
------------
1. Clone this repository or download the script file.
2. Install the required libraries:

How to Use
----------
1. Run the script in your Python environment (e.g., Jupyter Notebook, IDE, or terminal).
2. The script will:
- Fetch data for SPY, BTC, URTH, and QQQ from January 1, 2020, to November 11, 2024.
- Normalize and plot the data in two interactive charts:
  - One chart comparing all four assets.
  - Another chart comparing only SPY, URTH, and QQQ.
3. The interactive charts will open in your browser or Python environment, allowing for exploration by zooming and hovering over data points.

Code Explanation
----------------
- **Data Download**: Uses `yfinance.download()` to retrieve historical adjusted closing prices for each asset.
- **Data Normalization**: Normalizes data so that each asset starts at 100, enabling easy comparison.
- **Visualization**: Utilizes `plotly.graph_objects` to create interactive line charts.

Example Output
--------------
- **Chart 1**: Comparison of SPY, Bitcoin, MSCI World, and Nasdaq 100.
- **Chart 2**: Focused comparison of SPY, MSCI World, and Nasdaq 100.

License
-------
This project is licensed under the MIT License. You are free to use and modify it as needed.

Author
------

Alejandro Marco
