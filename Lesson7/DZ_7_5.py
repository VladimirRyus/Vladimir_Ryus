import os
import json

files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
size = max(files, key=lambda x: x[1])[1]

i = 1
out_dict = {}

for _ in range(len(str(size))):
    i *= 10
    out_dict[i] = (0, [])

for file in files:
    num, e_list = out_dict[10 ** len(str(file[1]))]
    e_list.append(file[0])
    e_list = list(set(e_list))
    out_dict[10 ** len(str(file[1]))] = (num + 1, e_list)

print(out_dict)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(out_dict, f_json)
