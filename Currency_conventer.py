import requests

API_KEY = "lMWvCltFuOSYWNt6cRxBmGbUEvfMStXV"

def currency_converter(from_currency, to_currency, amount):
    errors = []
    result = None

    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    
    conversion_result = response.json()

    if response.status_code == 200 and 'result' in conversion_result:
        result = conversion_result['result']
    else:
        errors.append("Failed to retrieve data.")

    return result, errors
