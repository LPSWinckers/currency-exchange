import os
import requests

api_key = "cur_live_6Mcs1nHLUbsS5wqlJJcizUiDUGjXJidmfigGdbTR"

def get_exchange_rate(from_currency, to_currency):
    """Returns the exchange rate from one currency to another."""
    url = f'https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies={to_currency}&base_currency={from_currency}'
    response = requests.get(url)
    return response.json()["data"][f"{to_currency}"]
