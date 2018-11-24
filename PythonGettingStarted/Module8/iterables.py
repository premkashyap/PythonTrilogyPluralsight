def is_prime(x):
    if x <2:
        return False
    for i in range(2,x):
        if x%i ==0:
            return False
    return True

iterable = [x for x in range(50) if is_prime(x)]
iterator = iter(iterable)
i = next(iterator)
try:
    while True:
        print(i)
        i = next(iterator)
except StopIteration as e:
    pass


