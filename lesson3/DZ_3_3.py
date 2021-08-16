def thesaurus(*names):
    dictionari = dict()
    for name in names:
        dictionari.setdefault(name[0], [])
        dictionari[name[0]].append(name)
    return dictionari
print(thesaurus("Иван", "Петр", "Илья", "Мария"))