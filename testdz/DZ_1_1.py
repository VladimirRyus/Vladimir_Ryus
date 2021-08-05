a = input ('Введите число')
a = int (a)

# Секунды
if a < 60:
    print (a, 'sec')

# Минуты
elif a < 1440:
    b =  a // 60
    c = a % 60
    print (b, 'min',c ,'sec')

# Часы
elif a < 34560:
    b = a // 3600
    c = a % 3600 // 60
    d = a % 60
    print (b, 'h', c, 'min',d ,'sec')

# Дни
elif a < 18144000:
    b = a // 86400
    c = a % 86400 // 3600
    d = a % 3600 // 60
    f = a % 60
    print (b, 'd',c, 'h', d, 'min', f, 'sec' )










