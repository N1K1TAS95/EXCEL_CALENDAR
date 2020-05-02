from datetime import date
from calendar import monthrange

week_days_names = {
    0: 'Lunedì',
    1: 'Martedì',
    2: 'Mercoledì',
    3: 'Giovedì',
    4: 'Venerdì',
    5: 'Sabato',
    6: 'Domenica'
}

year = int(input("Inserisci l'anno > "))
month = int(input('Inserisci il mese > '))

days = [["%02d/%02d/%d" % (x, month, year), week_days_names[date(year, month, x).weekday()]]
        for x in range(1, monthrange(year, month)[1] + 1)]

print(days)
    
