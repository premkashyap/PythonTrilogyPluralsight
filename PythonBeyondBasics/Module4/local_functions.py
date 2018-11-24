locals = []
def sort_by_last_letter(itr):
    def last_char(word):
        return word[-1]
    locals.append(last_char)
    return sorted(itr, key = last_char)

def func_returns_func():
    def inner_func(word):
        print(word[1:])
    return inner_func

def closure_ex():
    x = 5
    def inner_func(y):
        return x+y
    return inner_func


print(sort_by_last_letter(['prem', 'anita', 'raghu']))
print(sort_by_last_letter(['prem', 'anita', 'raghu']))
print(sort_by_last_letter(['prem', 'anita', 'raghu']))
print(locals)

f = func_returns_func()
f('Hello')

clos = closure_ex()
print(clos(10))
print(clos.__closure__)
