price = [55.4 , 42.9, 27.4, 12.3, 89.5, 79.3, 32.8, 66.9, 91.3, 5.5, 92.9, 6.5, 81.4, 18.1, 77.3, 29.5, 61.2, 30.9,
         50.5, 45.6]
for price_f in price:
    rub = int(price_f)
    kk = (price_f - rub) * 100
    print (f'{rub} рублей {kk:02.0f} копеек')

price = [55.4 , 42.9, 27.4, 12.3, 89.5, 79.3, 32.8, 66.9, 91.3, 5.5, 92.9, 6.5, 81.4, 18.1, 77.3, 29.5, 61.2, 30.9,
         50.5, 45.6]
print (id(price))
price.sort()
print (id(price))
for price_f in price:
    rub = int(price_f)
    kk = (price_f - rub) * 100
    print (f'{rub} рублей {kk:02.0f} копеек')

price = [55.4 , 42.9, 27.4, 12.3, 89.5, 79.3, 32.8, 66.9, 91.3, 5.5, 92.9, 6.5, 81.4, 18.1, 77.3, 29.5, 61.2, 30.9,
         50.5, 45.6]
for price_h in sorted(price)[::-1][:5]:
    rub = int(price_h)
    kk = (price_h - rub) * 100
    print(f'{rub} рублей {kk:02.0f} копеек')

