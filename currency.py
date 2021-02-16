from forex_python.converter import CurrencyRates

rates = CurrencyRates()

currency_codes = ['EUR', 'IDR', 'BGN', 'ILS' ,'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD',
                  'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD','THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK',
                  'BRL', 'PLN', 'PHP', 'ZAR']

help_string = ("\n|EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United Kingdom Pound |DKK - Denmark Krone \n\n"
                  "|CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar \n\n"
                  "|HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna \n\n"
                  "|NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso \n\n"
                  "|CZK - Czech Republic Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand\n")


def get_currencies():

    currency1 = input("Type the currency code of the currency you want to convert from (for example USD or EUR): ")

    while currency1.upper() not in currency_codes:
        print("That currency is not supported, choose another currency please")
        print("If you need help with currency codes type help")
        currency1 = input("Choose a supported currency: ")

        while currency1 == "help":
            print(help_string)
            currency1 = input("Choose a supported currency: ")

    currency2 = input("Type the currency code of the currency you want to convert to: ")

    while currency2.upper() not in currency_codes:
        print("That currency is not supported, choose another currency please")
        print("If you need help with currency codes type help")
        currency2 = input("Choose a supported currency: ")

        while currency2 == "help":
            print(help_string)
            currency2 = input("Choose a supported currency: ")

    return currency1,currency2


def converting(currency1,currency2):

    orig_amount = float(input("Enter the amount you want to convert: " ))

    converted_amount = rates.convert(currency1.upper(), currency2.upper(), orig_amount)

    print(orig_amount, currency1.upper(), "is", round(converted_amount, 2), currency2.upper())


if __name__ == '__main__':
    currency1, currency2 = get_currencies()
    converting(currency1, currency2)