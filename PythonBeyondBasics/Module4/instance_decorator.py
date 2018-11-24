class Tracer:
    def __init__(self):
        self.IsEnabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.IsEnabled:
                print('Tracing is happening')
            return f(*args, **kwargs)
        return wrap

tracer = Tracer()

@tracer
def rotate_list(lst):
    return lst[1:] +[lst[0]]

lst = [1,2,3]

print(rotate_list(lst))
tracer.IsEnabled = False
print(rotate_list(lst))

