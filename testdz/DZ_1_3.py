a = 'процент'
b = 'процента'
c = 'процентов'
for d in range (1, 101):
    x = d % 10
    if x ==1 and not (11 <= d <=14):
        print (d, a)
    elif 2 <= x <= 4 and not (11 <= d <= 14):
        print (d, b)
    elif 5 <= x <= 9 or x == 0 or (11 <= d <= 14):
        print (d, c)
