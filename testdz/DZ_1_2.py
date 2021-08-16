def sum (a):
     sum = 0
     while a:
          sum += a% 10
          a //= 10
     return sum

cubes = [a ** 3 for a in range (1, 1001, 2)]

sum_1 = 0
sum_2 = 0
for num in cubes:
     new_num = num + 17
     if sum (num) % 7 == 0:
          sum_1 += num
     if sum (new_num) % 7 == 0:
          sum_2 += new_num
print (sum_1)
print (sum_2)