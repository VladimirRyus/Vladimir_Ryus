dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def translate(eng):
    if eng[0] == eng[0].upper():
        eng = eng.lower()
        return dictionary[eng].capitalize()
    else:
        return dictionary[eng]

print(translate('five'))
print(translate('Ten'))
