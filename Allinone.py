from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "41ysUqRCsWqnH7xPKRbUnvpTwuxSrKC7"

@app.route('/', methods=['GET', 'POST'])
def currency_calculator():
    result = None
    errors = []

    if request.method == 'POST':
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = request.form['amount']

#currency_validation()
        try:
            amount = float(amount)
            if amount < 0:
                errors.append("Amount needs to be greater than 0.")
            if amount == 0:
                errors.append("Amound is equeal to 0")
        except:
            errors.append("Invalid amount.")

        if not errors:
            url ="https://api.apilayer.com/fixer/symbols"

            params = {
            "symbols": f"{from_currency},{to_currency}"
        }

            headers = {"apikey": API_KEY}

            response = requests.get(url, params=params, headers=headers)

            symbols = response.json().get('symbols', {})
            # print(symbols)
         
            if from_currency not in symbols:
                errors.append(f"The currency '{from_currency}' is not valid.")
            if to_currency not in symbols:
                errors.append(f"The currency '{to_currency}' is not valid.")

            if not errors:
                convert_url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
                response = requests.get(convert_url,params=params,headers=headers)
                conversion_result = response.json()

                if response.status_code == 200 and 'result' in conversion_result:
                    result = conversion_result['result']
                else:
                    errors.append("Failed to retrieve data.")

    return render_template('index.html', result=result, errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
