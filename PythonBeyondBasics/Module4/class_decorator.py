class call_count:
    def __init__(self, f):
        self.count = 0
        self.f = f
    def __call__(self, *args, **kwargs):
        self.count +=1
        self.f(*args, **kwargs)

@call_count
def func(name):
    print("Hello, {}".format(name))

func("Prem")
print(func.count)
func("Anita")
print(func.count)