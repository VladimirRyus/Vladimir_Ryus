with open('bakery.csv', 'w') as f:
    f.write('5978,5 \n 8914,3 \n 7879,1 \n 1573,7')

import sys

idx, val = sys.argv[1:]
with open('bakery.csv', 'r+') as f:
    file = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(f, 1):
        if i == int(idx):
            file.write(f'{val}\n')
            change = True
        else:
            file.write(line)
    if not change:
        exit('error')

    file.seek(0)

    f.truncate(0)
    for line in tmp_file:
        f.write(line)
    file.close()