from flask import Flask, request, render_template
from Currency_validation import currency_validation
from Amount_validation import amount_validation
from Currency_conventer import currency_converter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def currency_calculator():
    result = None
    errors = []

    if request.method == 'POST':
        from_currency = request.form['from_currency'].upper().strip()
        to_currency = request.form['to_currency'].upper().strip()
        amount = request.form['amount'].strip()

        amount, amount_errors = amount_validation(amount)
        errors.extend(amount_errors)

        if not errors:
            from_currency, to_currency, currency_errors = currency_validation(from_currency, to_currency)
            errors.extend(currency_errors)

        if not errors:
            result, conversion_errors = currency_converter(from_currency, to_currency, amount)
            errors.extend(conversion_errors)

    return render_template('index.html', result=result, errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
