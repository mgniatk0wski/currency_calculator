import requests
from datetime import datetime, timedelta

API_URL = "https://api.frankfurter.app"
CURRENCIES = [
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK",
    "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS",
    "INR", "ISK", "JPY", "KRW", "MXN", "MYR", "NOK",
    "NZD", "PHP", "PLN", "RON", "SEK",
    "SGD", "THB", "TRY", "USD", "ZAR"
]


def get_rate(base, target):
    if base == target:
        return 1.0
    try:
        response = requests.get(
            f"{API_URL}/latest",
            params={"base": base, "symbols": target},
            timeout=3
        )
        response.raise_for_status()
        data = response.json()
        return data["rates"][target]
    except Exception as e:
        print("API error:", e)
        return None


def get_historical_rates(base, target, days=30):
    end = datetime.now()
    start = end - timedelta(days=days)
    try:
        response = requests.get(
            f"{API_URL}/{start.date()}..{end.date()}",
            params={"base": base, "symbols": target},
            timeout=5
        )
        data = response.json()
        rates = data.get("rates", {})
        dates = sorted(rates.keys())
        values = [rates[date][target] for date in dates]
        return dates, values
    except Exception as e:
        print("API history error:", e)
        return [], []
