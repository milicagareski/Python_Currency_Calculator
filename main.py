import requests
from Currency_validation import currency_validation
from Amount_validation import amount_validation
from_currency,to_currency = currency_validation()
Amount = amount_validation()
import Currency_validation
import Amount_validation

url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={Amount}"

payload = {}
headers= {
  "apikey": "sYOvFbbasSjMOuH7UK27PNcwpOohXlkw"
  }
response = requests.request("GET", url, headers=headers, data = payload)
print("Converted amount will be: " + str(response.json()["result"]))
# Run this file for test