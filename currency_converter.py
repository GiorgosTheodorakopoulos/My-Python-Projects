def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            if amount <= 0:
                raise ValueError("Please enter a positive number.")
            return amount
        except ValueError:
            print("Invalid amount.")


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD','GBP')
    while True:
        currency = input(f"{label} currency (USD/EUR/CAD/GBP): ").upper()
        if currency not in currencies:
            print("Invalid currency.")
        else:
            return currency


def convert(amount, source_currency, target_currencies):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'CAD': 1.25, 'GBP': 0.75},
        'EUR': {'USD': 1.18, 'CAD': 1.47, 'GBP': 0.88},
        'CAD': {'USD': 0.80, 'EUR': 0.68, 'GBP': 0.63},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'CAD': 1.59},
    }

    converted_amounts = {}
    for target_currency in target_currencies:
        if source_currency == target_currency:
            converted_amounts[target_currency] = amount
        else:
            converted_amounts[target_currency] = exchange_rates[source_currency][target_currency] * amount

    return converted_amounts


def main():
    amount = get_amount()
    source_currency = get_currency('Source')

    target_currencies = []
    while True:
        target_currency = input("Enter target currencies separated by commas (EUR, CAD, USD, GBP): ").upper()
        target_currencies = [currency.strip() for currency in target_currency.split(',')]

        if all(currency in ('EUR', 'CAD', 'USD', 'GBP') for currency in target_currencies):
            break
        else:
            print("Invalid currency input. Please enter valid currencies.")

    converted_amounts = convert(amount, source_currency, target_currencies)

    print("\nConverted Amounts:")
    for currency, converted_amount in converted_amounts.items():
        print(f"{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {currency}")


if __name__ == '__main__':
    main()
