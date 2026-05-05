#  Exchange Rate Reporting System

A modular Python project that fetches real-time exchange rates from an external API, compares today’s and yesterday’s rates, calculates percentage changes, and generates a CSV report. It also includes structured logging and custom exception handling to support debugging, observability, and production-style execution.

##  Overview

This project is designed for automated exchange-rate monitoring and reporting. It retrieves currency conversion data, compares daily movement, flags significant changes, and stores the results in a CSV report for further analysis.

The codebase follows a modular structure with separate components for API access, report generation, logging, and exception handling.

##  Features

- Fetch exchange rates from an external API
- Compare today’s and yesterday’s rates
- Calculate percentage change for each currency
- Identify significant changes greater than 0.5%
- Generate CSV reports automatically
- Maintain structured log files with timestamps
- Use custom exception handling for easier debugging

##  Project Structure

```bash
EXCHANGE_RATE/
│
├── logs/                      # Stores log files
├── report/                    # Stores generated CSV reports
├── src/
│   ├── exception/
│   │   └── exception.py       # Custom exception handling
│   ├── logging/
│   │   └── logger.py          # Logging configuration
│   ├── exchange_rate_code/
│       ├── fetch_rates.py     # API calls for exchange rates
│       ├── generate_report.py # Report generation logic
│
├── main.py                    # Entry point
├── requirements.txt
```

##  Execution Flow

### 1. Entry Point (`main.py`)

The application starts from `main.py`, where the following inputs are defined:

- Base currency (default: `USD`)
- Date (default: current date)
- Currency list

It then calls the report creation logic.

### 2. Report Generation (`generate_report.py`)

This module:

- Creates the report directory if it does not exist
- Calls the rate-fetching function
- Computes:
  - Today’s rate
  - Yesterday’s rate
  - Percentage change
  - Significant change flag
- Saves the final output as a CSV file

### 3. Fetching Data (`fetch_rates.py`)

This module connects to the Frankfurter exchange rate API:

[Frankfurter API](https://api.frankfurter.dev/v2/rates)

It fetches:

- Today’s exchange rates
- Yesterday’s exchange rates
- API activity logs

### 4. Logging (`logger.py`)

The logging module:

- Creates timestamp-based log files
- Stores logs inside the `/logs/` directory
- Uses the format:

```text
time : level : message
```

### 5. Exception Handling (`exception.py`)

A custom exception class is used to capture:

- File name
- Line number
- Error message

This makes debugging easier, especially in production-style workflows.

## Output

The system generates a CSV report containing exchange-rate comparisons.

### Example CSV Output

```csv
currency,today_rate,yesterday_rate,% change,significant
INR,83.12,82.95,0.2048,No
EUR,0.92,0.91,1.0989,Yes
```

## How to Run

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the application

```bash
python main.py
```

## Configuration

Inside `main.py`, you can configure:

```python
BASE_CURRENCY = "USD"
USER_DATE = "2025-05-05"
CURRENCY = ["INR", "AED", "USD", "EUR", "GBP"]
```

You can modify:

- Base currency
- Date
- Currency list

## Logs

Log files are:

- Stored in `/logs/`
- Created separately for each run
- Useful for tracking:
  - API calls
  - Processing steps
  - Errors

## Error Handling

All exceptions are wrapped using `securityException`, which provides:

- Exact file location
- Line number
- Error message

This helps diagnose failures quickly and improves maintainability.

## Future Improvements

- Add database storage
- Add an API layer using FastAPI
- Add scheduling with Airflow or Cron
- Add a visualization dashboard using Streamlit

## Author

Developed as a modular and production-ready pipeline for real-world exchange rate monitoring and reporting.
