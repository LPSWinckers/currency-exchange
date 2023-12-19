import requests

api_key = "fca_live_TkJkw5715P9KGDkWBgnIPY8brYjVu858KbO3tY24"

def get_exchange_rate(from_currency, to_currency):
    if from_currency == to_currency:
        return 1
    elif from_currency == "USD":
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies={to_currency}"
    else:
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies={to_currency}&base_currency={from_currency}"

    respone = requests.get(url)

    return respone.json()
