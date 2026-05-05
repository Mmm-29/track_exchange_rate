

import requests
import sys
from datetime import date, timedelta, datetime
from src.exception.exception import securityException
from src.logging.logger import logger

API_URL = "https://api.frankfurter.dev/v2/rates"


def fetch_exchange_rates(base_currency, currencies, date_str=None):
    try:
        

        params = {
            "base" : base_currency,
            "quotes" : ",".join(currencies)
        }
        if date_str:
            params["date"] = date_str
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
 
        data = response.json()
        rate = {}

        for i in data:
            quote_currency = i["quote"]
            rate[quote_currency] = i["rate"]

        return rate
    except Exception as e:
        raise securityException(e, sys) from e


def fetch_today_yesterday_rates(base_currency, currencies, date_str=None):
    try:

        select_date = (
        datetime.strptime(date_str, "%Y-%m-%d") if date_str
        else datetime.today()
        )

        logger.info("Fetching exchange rates for base currency: {} and quote currencies: {} and date: {}".format(base_currency, currencies, select_date.strftime("%Y-%m-%d")))

        
        

        # Today rates
        today_rate = fetch_exchange_rates(base_currency, currencies,date_str)

        # Yesterday date
        yesterday = select_date - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y-%m-%d")

        # Yesterday rates
        yest_rate = fetch_exchange_rates(
            base_currency,
            currencies,
            yesterday_str
        )

        logger.info("Fetched today's and yesterday's exchange rates successfully.")
        logger.info("Fetched {} rates : {}".format(select_date.strftime("%Y-%m-%d"), today_rate))
        logger.info("Fetched {} rates : {}".format(yesterday_str, yest_rate))

        return today_rate, yest_rate
    
    except Exception as e:
        raise securityException(e, sys) from e

"""
To run thi Script 
    BASE_CURRENCY = "USD"
    CURRENCIES = ["INR", "AED", "USD", "EUR", "GBP", "BRL", "MXN"]
    today_rate, yest_rate = fetch_today_yesterday_rates(BASE_CURRENCY, CURRENCIES)
    print("Today Rate:\n{}".format(today_rate))
    print("\nYesterday Rate:\n{}".format(yest_rate))

"""