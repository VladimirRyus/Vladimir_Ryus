def thesaurus_adv(*names_surnames):
    dictionary = dict()
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        dictionary.setdefault(surname[0], {})
        dictionary[surname[0]].setdefault(name[0], [])
        dictionary[surname[0]][name[0]].append(name_surname)

    sort_dict = {x: dictionary[x] for x in sorted(dictionary)}
    return dictionary

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))