def gen(max_num):
    n = 1
    while n <= num:
        yield n
        n += 3
odd_to_30 = gen (30)
