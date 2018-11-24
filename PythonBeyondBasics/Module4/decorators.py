import functools
def decor1(f):
    @functools.wraps(f) #this takes the metadata like __name__ and __doc__ of f and asign them to wrap. 
    def wrap(*args, **kwargs):
        x= f(*args, **kwargs)
        return x[1:]
    return wrap

def decor2(f):
    def wrap(*args, **kwargs):
        x= f(*args, **kwargs)
        return x[2:]
    return wrap


@decor2
@decor1
def printer1():
    return "Prem"

    

print(printer1())
