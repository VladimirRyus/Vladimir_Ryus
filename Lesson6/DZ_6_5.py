import sys
from itertools import zip_longest
user, hobby, out = sys.argv[1:]
with open(out, 'w', encoding='utf-8') as f:
    with open(user, encoding='utf-8') as user:
        with open(hobby, encoding='utf-8') as hobby:
            n_lines_user = sum(1 for line in user)
            n_lines_hobby = sum(1 for line in hobby)

            if n_lines_users < n_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}: '
                        f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
