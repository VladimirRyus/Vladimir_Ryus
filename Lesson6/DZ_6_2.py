with open('nginx_logs.txt') as f:
    file = []
    spammer = {}
    for line in f:
        splitted = line.split()
        file.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spammer.setdefault(splitted[0], 0)
        spammer [splitted[0]] += 1
spammer = sorted(spammer.items(), key=lambda x: x[1], reverse=True)
print (spammer [:5])

        







