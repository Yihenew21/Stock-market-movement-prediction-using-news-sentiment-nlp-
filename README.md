# Stock Market Movement Prediction Using News Sentiment and Quantitative Analysis

## Project Overview

This project analyzes financial news and stock price data to discover correlations between news sentiment and stock market movements. It demonstrates skills in Data Engineering, Financial Analytics, and Machine Learning Engineering.

**Key tasks completed:**

- Modular Exploratory Data Analysis (EDA) on news data
- Quantitative analysis of stock price data using TA-Lib and PyNance
- Visualizations of technical indicators and financial metrics

## Folder Structure

```
├── .vscode/
├── .github/
│   └── workflows/
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── eda_descriptive.py
│   ├── eda_text.py
│   ├── eda_time.py
│   ├── eda_publisher.py
│   ├── quant_data.py
│   └── quant_indicators.py
├── notbooks/
│   ├── eda_analyst_ratings.ipynb
│   └── quant_analysis.ipynb
├── data/
│   ├── raw_analyst_ratings.csv
│   └── yfinance_data/
├── scripts/
├── tests/
```

## Setup Instructions

1. **Clone the repository and create a virtual environment:**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. **Install TA-Lib (Windows):**
   - Download the appropriate TA-Lib wheel from [Gohlke's site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib) and install it:
     ```sh
     pip install TA_Lib‑0.4.0‑cp3xx‑cp3xx‑win_amd64.whl
     pip install ta-lib
     ```
3. **Install PyNance:**
   ```sh
   pip install pynance
   ```
4. **(Optional) Install Jupyter kernel for your venv:**
   ```sh
   pip install ipykernel
   python -m ipykernel install --user --name=venv --display-name="Python (venv)"
   ```

## Usage

- Run the EDA notebook: `notbooks/eda_analyst_ratings.ipynb`
- Run the quantitative analysis notebook: `notbooks/quant_analysis.ipynb`

## Completed Tasks

### Task 1: EDA on Analyst Ratings Dataset

- Modularized EDA code for descriptive stats, text analysis, time series, and publisher analysis
- Jupyter notebook demonstrating EDA workflow

### Task 2: Quantitative Analysis

- Modularized code for loading and preparing yfinance stock data
- Calculation of technical indicators (SMA, EMA, RSI, MACD) using TA-Lib
- Calculation of financial metrics (returns, volatility) using PyNance
- Visualizations for all metrics and indicators

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- nltk
- spacy
- jupyter
- ta-lib
- pynance

See `requirements.txt` for details.
