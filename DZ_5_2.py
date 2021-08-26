max = 5
num_gen = (n for n in range(1, max + 1, 2))
print (next(num_gen))
print (*num_gen) #Проверка что остальные элементы тоже генерируются
