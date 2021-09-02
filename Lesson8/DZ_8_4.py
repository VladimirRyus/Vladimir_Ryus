from functools import wraps


def checker(decorator):
    def checker(func_cube):
        @wraps(func_cube)
        def wrapped(x):
            if decorator(x):
                return func_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return checker


@checker(lambda x: x > 0)
def calc_cube(x):
    """calc_cube desc"""
    return x ** 3


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)