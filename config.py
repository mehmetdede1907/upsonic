# config.py

def get_company_names():
    """
    Prompts the user to enter company ticker symbols and returns them as a list.
    """
    user_input = input("Enter the company ticker symbols separated by commas (e.g., AAPL, GOOG, MSFT): ")
    if not user_input:
        print("No input provided, using default companies: AAPL, GOOG, ORCL")
        return ["AAPL", "GOOG", "ORCL"]
    return [name.strip().upper() for name in user_input.split(",") if name.strip()]

COMPANY_NAMES = get_company_names()