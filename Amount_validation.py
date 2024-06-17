def amount_validation(amount):
    errors = []
    try:
        amount = float(amount)
        if amount <= 0:
            errors.append("Amount needs to be greater than 0.")
    except ValueError:
        errors.append("Invalid amount.")
    
    return amount, errors
