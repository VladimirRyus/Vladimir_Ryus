with open('nginx_logs.txt') as f:
    file = []
    for line in f:
        splitted = line.split()
        file.append ((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(file)