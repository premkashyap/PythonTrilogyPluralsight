def check_non_negative(i):
    def validator(f):
        def wrap(*args):
            if args[i] < 0:
                raise ValueError('Size can\'t be negative')
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value, size):
    return [value]*size

print(create_list('a', 3))
print(create_list('b', -1))