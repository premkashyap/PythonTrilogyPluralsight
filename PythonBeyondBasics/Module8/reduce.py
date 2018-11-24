from functools import reduce
import operator

print(reduce(operator.add, [1,2,3,4,5]))

def mul(x,y):
    print("mul {}, {}".format(x,y))
    return x*y
reduce(mul, [1,2,3,4,5,6], 10)