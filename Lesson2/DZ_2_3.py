list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

idx = 0
while idx < len (list1):
    if list1[idx].isdigit():
        list1.insert (idx, '"')
        list1[idx + 1] = f'{int(list1[idx + 1]):02}'
        list1.insert (idx + 2, '"')
        idx += 2
    elif (list1[idx].startswith('+') or list1[idx].startswith('-')) and list1[idx][1:].isdigit():
        list1.insert(idx, "'")
        list1[idx + 1] = f'{list1[idx + 1][0]} {int(list1[idx + 1]):02}'
        idx +=2
    idx += 1
info = ' '.join(list1)

idx_s = []
for idx, let in enumerate(info):
    if let == '"':
        idx_s.append (idx)

for idx in range(len(idx_s)):
    if idx % 2 == 0:
        idx_s[idx] = idx_s[idx] + 1
    else:
        idx_s[idx] = idx_s[idx] - 1

for idx_d in reversed(idx_s):
    info = info [:idx_d] + info[idx_d + 1:]
print (info)









