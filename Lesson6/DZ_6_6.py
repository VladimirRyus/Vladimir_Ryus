import sys

price = sys.argv[1:]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')

import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start = int(nums[0])
        end = int(nums[1])
    elif len(nums) == 0:
        start = 0
        end = sum(1 for line in f)
        f.seek(0)
    else:
        start = int(nums[0])
        end = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start <= idx + 1 <= end:
            print(line.strip())