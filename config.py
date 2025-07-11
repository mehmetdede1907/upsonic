# config.py

import os

def get_company_names():
    """
    Gets company ticker symbols from environment variable or uses defaults.
    In containerized environments, uses environment variable COMPANY_TICKERS.
    """
    # Check if running in container (environment variable exists)
    company_tickers = os.getenv('COMPANY_TICKERS')
    
    if company_tickers:
        return [name.strip().upper() for name in company_tickers.split(",") if name.strip()]
    else:
        # Default companies if no environment variable is set
        print("No COMPANY_TICKERS environment variable found, using default companies: AAPL, GOOG, ORCL")
        return ["AAPL", "GOOG", "ORCL"]

COMPANY_NAMES = get_company_names()