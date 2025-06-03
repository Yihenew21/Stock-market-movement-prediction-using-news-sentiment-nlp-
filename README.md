# Stock Sentiment Correlation Analysis

This repository contains a Python-based project to analyze the correlation between news sentiment and stock price movements for seven stocks (AAPL, AMZN, GOOG, META, MSFT, NVDA, TSLA). The project uses VADER for sentiment analysis of news headlines and computes Pearson correlations (contemporaneous and lagged) between sentiment scores and stock price indicators, with Granger causality tests to assess predictive relationships.

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Continuous Integration](#continuous-integration)
- [License](#license)

## Project Overview

The project investigates whether news sentiment from analyst ratings influences stock price movements. Key steps include:

- Scoring news headlines from `raw_analyst_ratings.csv` using VADER sentiment analysis.
- Aggregating sentiment scores by date.
- Merging with stock price data from Yahoo Finance (stored in `data/yfinance_data/*.csv`).
- Computing correlations between sentiment and price indicators (e.g., daily returns, closing prices).
- Visualizing results with heatmaps.
- Performing Granger causality tests to explore predictive relationships.

The analysis is implemented in a Jupyter Notebook (`notebooks/correlation_analysis.ipynb`) with modular code in `src/` for sentiment analysis and correlation computations.

## Repository Structure

```
stock-sentiment-analysis/
├── data/
│   ├── raw_analyst_ratings.csv        # News headlines dataset
│   └── yfinance_data/
│       ├── AAPL_historical_data.csv   # Stock price data for AAPL
│       ├── AMZN_historical_data.csv   # Stock price data for AMZN
│       ├── GOOG_historical_data.csv   # Stock price data for GOOG
│       ├── META_historical_data.csv   # Stock price data for META
│       ├── MSFT_historical_data.csv   # Stock price data for MSFT
│       ├── NVDA_historical_data.csv   # Stock price data for NVDA
│       └── TSLA_historical_data.csv   # Stock price data for TSLA
├── notebooks/
│   └── correlation_analysis.ipynb     #  Jupyter Notebook for analysis
│   ├── eda_analyst_ratings.ipynb      #  Jupyter Notebook for analysis
│   └── quant_analysis.ipynb           #  Jupyter Notebook for analysis
├── src/
│   ├── sentiment_analysis.py          # Functions for VADER sentiment scoring
│   └── correlation_analysis.py
│   ├── eda_descriptive.py
│   ├── eda_text.py
│   ├── eda_time.py
│   ├── eda_publisher.py
│   ├── quant_data.py
│   └── quant_indicators.py        # Functions for merging data and computing correlations
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions workflow for CI
├── .gitignore                        # Git ignore file for temporary files
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation (this file)
└── LICENSE                           # License file
```

## Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Git (for version control)
- A virtual environment tool (e.g., `venv` or `virtualenv`)

Required Python packages are listed in `requirements.txt`.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/stock-sentiment-analysis.git
   cd stock-sentiment-analysis
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Data**:
   Ensure `data/raw_analyst_ratings.csv` and `data/yfinance_data/*.csv` are present. The stock CSV files should contain columns: `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`, `Dividends`, `Stock Splits`.

## Usage

1. **Launch Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

   Navigate to the `notebooks/` folder and open `correlation_analysis.ipynb`.

2. **Run the Notebook**:

   - Execute cells sequentially to:
     - Load news and stock data from `data/`.
     - Score news headlines for sentiment using `src/sentiment_analysis.py`.
     - Aggregate sentiment by date.
     - Merge with stock price data using `src/correlation_analysis.py`.
     - Compute and visualize correlations.
     - Perform Granger causality tests.
   - Debug outputs in Sections 1, 3, 4, and 5 help verify data integrity (e.g., column names, date ranges).

3. **Customize Analysis**:
   - Update `text_col` in Section 2 if the news headline column is not `headline` (e.g., `title`).
   - Modify `possible_price_cols` in Section 6 to include additional price indicators (e.g., `Close`, `Adj Close`).
   - Adjust lag periods in Section 9 for lagged correlations.

## Data Sources

- **News Data**: `data/raw_analyst_ratings.csv` contains analyst ratings with a `date` column (datetime) and a `headline` column (text). Ensure the dataset covers the desired time period.
- **Stock Data**: CSV files in `data/yfinance_data/` are sourced from Yahoo Finance via `yfinance`. Each file includes daily price data with `Date`, `Close`, and `Adj Close` columns.

**Note**: Ensure date ranges overlap between news and stock data for meaningful correlations. Check debug outputs in `notebooks/correlation_analysis.ipynb` (Sections 3 and 4) for date range alignment.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes with clear messages (see [Commit Message Guidelines](#commit-message-guidelines)).
4. Push to your fork (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description.

Follow the code style in `src/` (PEP 8 for Python) and include tests for new functions.

## Commit Message Guidelines

To maintain a clear commit history, follow these guidelines:

- **Format**: Use the imperative mood with a structured format:
  ```
  <type>(<scope>): <short description>
  ```
  - Types: `feat` (new feature), `fix` (bug fix), `docs` (documentation), `refactor` (code improvement), `test` (add tests), `chore` (maintenance).
  - Scope: Affected module (e.g., `notebook`, `sentiment`, `correlation`, `readme`).
  - Example: `fix(notebook): Handle date type mismatch in merge step`
- **Details**: Include a longer description if needed, explaining _what_ changed and _why_.
- **References**: Link to issues or pull requests (e.g., `Closes #123`).
- **Example**:
  ```
  docs(readme): Update README with notebooks folder structure
  Reflect updated project structure with notebooks/ and src/ folders.
  Addresses feedback on repository best practices.
  ```

## Continuous Integration

This project uses GitHub Actions for continuous integration (CI). The workflow (`.github/workflows/ci.yml`) runs on every push and pull request to:

- Check code style with `flake8` for `src/` files.
- Run unit tests for modular components in `src/` (if tests are added).
- Verify notebook execution with `nbval` to ensure `notebooks/correlation_analysis.ipynb` runs without errors.

To add tests:

1. Create test files in `src/` (e.g., `test_sentiment_analysis.py`).
2. Update `ci.yml` to include test commands (e.g., `pytest src/`).

**Sample CI Workflow** (`.github/workflows/ci.yml`):

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.8"
      - run: pip install -r requirements.txt
      - run: pip install flake8 nbval
      - run: flake8 src/
      - run: jupyter nbconvert --to notebook --execute notebooks/correlation_analysis.ipynb
```

**Future Improvements**:

- Add test coverage reports with `pytest-cov`.
- Integrate static type checking with `mypy`.
- Expand tests for edge cases (e.g., missing columns, invalid dates).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

_Last Updated: June 3, 2025_
