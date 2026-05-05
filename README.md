#  Exchange Rate Reporting System

##  Overview

A modular Python project that fetches real-time exchange rates from an external API, compares today’s and yesterday’s rates, calculates percentage changes, and generates a CSV report.

The system also includes:

* Structured logging
* Custom exception handling
* Automated scheduling (Windows Task Scheduler)

Designed to mimic **production-grade data pipelines** with modular architecture and observability.

---

##  Features

*  Fetch exchange rates from external API
*  Compare today vs yesterday
*  Percentage change calculation
*  Detect significant changes (>0.5%)
*  Automated CSV report generation
*  Structured logging system
*  Custom exception handling
*  Automated daily execution (Scheduler)

---

##  Project Structure

```
EXCHANGE_RATE/
│
├── logs/                      # Log files
├── report/                    # CSV reports
├── src/
│   ├── exception/
│   │   └── exception.py
│   ├── logging/
│   │   └── logger.py
│   ├── exchange_rate_code/
│       ├── fetch_rates.py
│       ├── generate_report.py
│
├── main.py                    # Entry point
├── scheduler_task.py          # Task scheduler (Windows)
├── requirements.txt
```

---

##  Execution Flow

### 1️ Entry Point (`main.py`)

* Accepts:

  * Base currency (default: USD)
  * Date
  * Currency list
* Calls report generation logic

---

### 2️ Report Generation (`generate_report.py`)

* Creates report directory if not exists
* Fetches rate data
* Computes:

  * Today rate
  * Yesterday rate
  * % change
  * Significant flag
* Saves CSV report

---

### 3️ Fetching Data (`fetch_rates.py`)

* Uses API:

  ```
  https://api.frankfurter.dev/v2/rates
  ```
* Retrieves:

  * Today’s rates
  * Yesterday’s rates

---

### 4️ Logging (`logger.py`)

* Stores logs in `/logs/`
* Format:

  ```
  time : level : message
  ```

---

### 5️ Exception Handling (`exception.py`)

Custom `securityException` captures:

* File name
* Line number
* Error message

---

### 6️ Scheduler (`scheduler_task.py`)

This script automates daily execution using **Windows Task Scheduler**.

####  Code

```python
import subprocess

TASK_NAME = "ExchangeRateFetchingTaskDaily"
PYTHON_PATH = r"D:\exchange_rate\virtual_env\Scripts\python.exe"
PROJECT_DIR = r"D:\exchange_rate"
SCRIPT_NAME = "main.py"

SCHEDULE_TIME = "11:06"

command = (
    f'schtasks /create /sc DAILY /tn "{TASK_NAME}" '
    f'/tr "cmd /c cd /d {PROJECT_DIR} && {PYTHON_PATH} {SCRIPT_NAME}" '
    f'/st {SCHEDULE_TIME} /f'
)

subprocess.run(command, shell=True)

print("Task Scheduled Successfully!")
```

---

###  How Scheduler Works

* Uses Windows command: `schtasks`
* Runs script daily at specified time
* Automatically triggers:

  ```
  python main.py
  ```

---

## 📊 Output

Example CSV:

```
currency,today_rate,yesterday_rate,% change,significant
INR,83.12,82.95,0.2048,No
EUR,0.92,0.91,1.0989,Yes
```

---

##  How to Run

### 1️ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️ Run manually

```bash
python main.py
```

### 3️ Setup scheduler (Windows)

```bash
python scheduler_task.py
```

---

##  Configuration

Inside `main.py`:

```python
BASE_CURRENCY = "USD"
USER_DATE = "2025-05-05"
CURRENCY = ["INR", "AED", "USD", "EUR", "GBP"]
```

---

##  Logs

* Stored in `/logs/`
* New log file per run
* Tracks:

  * API calls
  * Processing steps
  * Errors

---

##  Error Handling

All exceptions are wrapped using `securityException`:

* File location
* Line number
* Error message

---

##  Future Improvements

*  Database integration
*  FastAPI API layer
*  Airflow / Cron scheduling (cross-platform)
*  Streamlit dashboard

---

