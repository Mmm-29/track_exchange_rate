from datetime import datetime
import sys
from src.exchange_rate_code.fetch_rates import fetch_today_yesterday_rates
from src.exchange_rate_code.generate_report import create_report
from src.logging.logger import logger
from src.exception.exception import securityException
from datetime import datetime


# BASE_CURRENCY = input("Enter base currency: ").upper()
BASE_CURRENCY = "USD"
# USER_DATE = input("Enter date (YYYY-MM-DD) or press Enter for today's rates: ")
USER_DATE = datetime.today().strftime("%Y-%m-%d")
CURRENCY = ["INR", "AED", "USD", "EUR", "GBP", "BRL", "MXN"]


def main():

    try:
        logger.info("Fetching exchage rates process started.....")
        logger.info("User input - Base Currency: {}".format(BASE_CURRENCY))
        logger.info(
        "User input - Date: {}".format(
            USER_DATE if USER_DATE else datetime.today()
        )
    )

        base_currency = BASE_CURRENCY
        currencies = CURRENCY

        create_report(base_currency, currencies, USER_DATE)

        logger.info("Fetching rates and creating report process completed successfully.")
    except Exception as e:
        logger.exception("Main process failed")
        raise


if __name__ == "__main__":
    main()