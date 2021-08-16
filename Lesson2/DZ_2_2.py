list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = []
for elem in list1:
    if elem.isdigit():
        list2.extend (['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem [1:].isdigit():
        list2.extend (['"', f'{elem[0]}{int (elem[1:]):02}', '"'])
    else:
        list2.append(elem)

info = ' '.join(list2)
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



