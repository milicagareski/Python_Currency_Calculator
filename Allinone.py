from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "41ysUqRCsWqnH7xPKRbUnvpTwuxSrKC7"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    errors = None

    if request.method == 'POST':
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = request.form['amount']

        # Validate currencies
        symbols_url ="https://api.apilayer.com/fixer/symbols"
        headers = {"apikey": API_KEY}
        response = requests.get(symbols_url, headers=headers)
        symbols = response.json().get('symbols', {})

        errors = []
        if from_currency not in symbols:
            errors.append(f"The currency '{from_currency}' is not valid.")
        if to_currency not in symbols:
            errors.append(f"The currency '{to_currency}' is not valid.")

        if not errors:
            # Convert currency
            convert_url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
            response = requests.get(convert_url, headers=headers)
            print(response)
            conversion_result = response.json()

            if response.status_code == 200 and 'result' in conversion_result:
                result = conversion_result['result']
            else:
                errors.append("Conversion failed. Please check the currency codes and try again.")

    return render_template('index.html', result=result, errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
