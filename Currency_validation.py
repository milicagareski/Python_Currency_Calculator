import requests

def currency_validation():
    while True:
        from_currency = input(" Enter currency to be converted from:  ").upper()
        to_currency = input(" Enter currency to be converted to:  ").upper()

        url = "https://api.apilayer.com/fixer/symbols"
        api_key = "sYOvFbbasSjMOuH7UK27PNcwpOohXlkw"

        params = {
            "symbols": f"{from_currency},{to_currency}"
        }

        headers = {
            "apikey": api_key
        }

        response = requests.get(url, params=params, headers=headers)

        status_code = response.status_code
        result = response.json()

        if status_code == 200:
            if from_currency in result["symbols"]:
                if to_currency in result["symbols"]:
                    
                    break
                else:
                    print(f"The currency '{to_currency}' is not valid.")
            elif to_currency in result["symbols"]:
                print(f"1 {from_currency} is equal to {result['symbols'][to_currency]} {to_currency}.")
                break
            elif from_currency not in result["symbols"]:
                print(f"The currency '{from_currency}' is not valid.")
            elif to_currency not in result["symbols"]:
                print(f"The currency '{to_currency}' is not valid.")
        else:
            print("Failed to retrieve data.")

currency_validation()