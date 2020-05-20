import datetime
from forex_python.converter import CurrencyRates
from decimal import Decimal
from soupsieve.util import upper

def checkCurrency(curr):
    check = {u'IDR', u'BGN', u'ILS', u'GBP', u'DKK', u'CAD', u'JPY', u'HUF', u'RON', u'MYR',
             u'SEK', u'SGD', u'HKD', u'AUD', u'CHF', u'KRW', u'CNY', u'TRY', u'HRK', u'NZD',
             u'THB', u'EUR', u'NOK', u'RUB', u'INR', u'MXN', u'CZK', u'BRL', u'PLN', u'PHP', u'ZAR', u'USD'}
    return curr in check


def isfloat(value):
   try:
    float(value)
    return True
   except ValueError:
    return False


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def get_history():
    fout = open('convert_operation.txt', 'r')
    text = fout.read()
    fout.close()
    return text

c = CurrencyRates()
date_obj = datetime.datetime.now()
flag = True
innerflag = True
retsecpectiveFlag = False
while flag:
    while innerflag:
        print('Enter the currency that needs to be converted: ', end='')
        currencyOld = input()
        currencyOld = upper(currencyOld)
        if checkCurrency(currencyOld):
            break
        else:
            print('Incorrect currency. Try again.')
    while innerflag:
        print('Enter the result currency: ', end='')
        currencyNew = input()
        currencyNew = upper(currencyNew)
        if checkCurrency(currencyNew):
            break
        else:
            print('Incorrect currency. Try again.')
    while innerflag:
        print('Enter the amount: ', end='')
        amount = input()
        if isfloat(amount):
            amount = float(amount)
            break
        else:
            print('Incorrect amount. Try again.')
    print('Date:', datetime.datetime.now().date())
    print('Enter date or press Enter to continue: ', end='')
    date_str = input()
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        retsecpectiveFlag = True
    except ValueError as ve:
        date_obj = datetime.datetime.now()
    except TypeError as te:
        date_obj = datetime.datetime.now()
        if len(date_str) != 0:
            print('!Wrong date, selected by default.')
    print()
    print(currencyOld, amount, 'to', currencyNew, 'is ', end='')
    print(toFixed(c.convert(currencyOld, currencyNew, amount, date_obj), 2))
    print()
    fin = open('convert_operation.txt', 'a')
    if retsecpectiveFlag:
        print('retrospective:', date_obj, '|', sep='', end='', file=fin)
        print('convert_operation:', currencyOld, amount, 'to', currencyNew, 'is ', end='', file=fin)
        retsecpectiveFlag = False
    else:
        print('convert_operation:', currencyOld, amount, 'to', currencyNew, 'is ', end='', file=fin)
    print(toFixed(c.convert(currencyOld, currencyNew, amount, date_obj), 2), '|RATE:', toFixed(c.get_rate(currencyOld, currencyNew, date_obj), 2), '|DATE:', datetime.datetime.now().date(), file=fin)
    fin.close()

    print('Press', '1.New convert', '2.Get history', '3.Exit', sep='\n')
    menu = input()
    #можно использовать switch
    if menu is '1':
        continue
    elif menu is '2':
        print(get_history())
        print('Press Enter to continue')
        pause = input()
    else:
        flag = False
