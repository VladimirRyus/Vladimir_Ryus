import re
MAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def parse (email):
    found_info = MAIL.findall(email)[0]
    if found_info:
        name, addr = found_info
    else:
        raise ValueError(f'check adress: {email}')
    print(name, addr)

parse('someone@geekbrains.ru')
parse('someone@geekbrainsru')

