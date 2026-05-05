import pandas as pd
import os,sys
from src.exchange_rate_code.fetch_rates import fetch_today_yesterday_rates
from src.logging.logger import logger
from src.exception.exception import securityException
from datetime import datetime

BASE_DIR = os.getcwd()
REPORT_DIR = os.path.join(BASE_DIR, "report")
os.makedirs(REPORT_DIR, exist_ok=True)




def create_report(base_currency, currencies, date_str=None):
    try:
        

        if date_str:
            file_date = date_str
        else:
            file_date = datetime.today().strftime("%Y-%m-%d")

        CSV_FILE = os.path.join(
            REPORT_DIR,
            "exchange_rate_report_{}.csv".format(file_date)
        )


        today_rate, yest_rate = fetch_today_yesterday_rates(base_currency, currencies, date_str)

        logger.info("Started report generation.....")

        rows = []
        for curr in currencies:
            t_rate = today_rate.get(curr)
            y_rate = yest_rate.get(curr)


            if t_rate is not None and y_rate is not None:
                pct_change = ((t_rate - y_rate) / y_rate) * 100
                significant_change = "Yes" if abs(pct_change) > 0.5 else "No"

                
                rows.append({
                "currency": curr,
                "today_rate": round(t_rate, 6),
                "yesterday_rate": round(y_rate, 6),
                "% change": round(pct_change, 4),
                "significant": significant_change
                })
        logger.info("Percentage chage calculation completed.")

        df = pd.DataFrame(rows)
        df.to_csv(CSV_FILE, index=False)
        logger.info("CSV Generated Successfully at {}".format(CSV_FILE))

    except Exception as e:
        
        raise securityException(e, sys) from e