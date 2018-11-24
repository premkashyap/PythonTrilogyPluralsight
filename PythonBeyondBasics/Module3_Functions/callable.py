from classes_as_functions import Resolver 

def is_even(x):
    return x%2

print(callable(Resolver))
print(callable(lambda: print('Hey')))
print(callable(is_even))
print(callable(Resolver().clear))