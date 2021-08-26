from itertools import  zip_longest
with open('task1.txt', 'w', encoding='utf-8') as f:
    with open('user.csv', encoding='utf-8') as user:
        with open('hobby.csv', encoding='utf-8') as hobby:
            n_line_user = sum(1 for line in user)
            n_line_hobby = sum(1 for line in hobby)
            if n_line_user < n_line_hobby:
                exit(1)

            user.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(user, hobby):
                f.write(f'{line_user.strip()}: ' 
                        f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
