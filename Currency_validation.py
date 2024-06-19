import requests

API_KEY = "lMWvCltFuOSYWNt6cRxBmGbUEvfMStXV"

def currency_validation(from_currency, to_currency):
    errors = []

    url = "https://api.apilayer.com/fixer/symbols"

    params = {
            "symbols": f"{from_currency},{to_currency}"
        }

    headers = {"apikey": API_KEY}

    response = requests.get(url,params=params, headers=headers)

    # result = response.json().get('symbols', {})

    result_j = response.json()
    if 'symbols' in result_j:
        result = result_j['symbols']
    else:
        result = {}
    
    # print(result)

    if from_currency not in result:
        errors.append(f"The currency '{from_currency}' is not valid.")
    if to_currency not in result:
        errors.append(f"The currency '{to_currency}' is not valid.")

    return from_currency, to_currency, errors
