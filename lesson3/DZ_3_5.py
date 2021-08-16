import random

word1 = ["автомобиль", "лес", "огонь", "город", "дом"]
word2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
word3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    list = []
    for a in range (num):
        c_word1 = random.choice(word1)
        c_word2 = random.choice(word2)
        c_word3 = random.choice(word3)
        list.append (f'{c_word1} {c_word2} {c_word3}')
    return list

print(get_jokes(1))
print(get_jokes(2))

def get_jokes_adv (num, repeats=True):
    list = []
    if not repeats:
        if num > min(len(word1), len(word2), len(word3)):
            return  'No way'
        else:
            random.shuffle(word1)
            random.shuffle(word2)
            random.shuffle(word3)
            for a in range(num):
                list.append(f'{word1[a]} {word2[a]} {word3[a]}')

    else:
        for a in range(num):
            c_word1 = random.choice(word1)
            c_word2 = random.choice(word2)
            c_word3 = random.choice(word3)
            list.append(f'{c_word1} {c_word2} {c_word3}')
        return list

print(get_jokes_adv(4, False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))


















