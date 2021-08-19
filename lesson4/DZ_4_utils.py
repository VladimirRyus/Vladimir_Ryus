import requests
from decimal import *
from datetime import datetime

getcontext().prec = 4


def current_rates(valute):
    valute = valute.upper()
    responce = requests.get ('http://www.cbr.ru/scripts/XML_daily.asp').text

    if valute not in responce:
        return None

    rub = responce[responce.find('<Value>', responce.find(valute)) + 7:responce.find('</Value>', responce.find(valute))]
    day_raw = responce[responce.find('Date="') + 6:responce.find('"', responce.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"



print(current_rates('USD'))

