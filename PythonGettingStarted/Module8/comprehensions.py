import math

def is_prime(x):
    if x <2:
        return False
    for i in range(2,x):
        if x%i ==0:
            return False
    return True

list1 = "The quick brown fox jumps over the lazy dog".split()
list2 = [len(word) for word in list1]
list3 = [len(str(math.factorial(x))) for x in range(20)]
tupl1 = {len(str(math.factorial(x))) for x in range(20)}
dict1 = {x:len(str(math.factorial(x))) for x in range(20)}
print(list3)
print(tupl1)
print(dict1)

list3 = [x for x in range(50) if is_prime(x)]
tupl1 = {x for x in range(50) if is_prime(x)}
dict1 = {x:(1, x, x*x) for x in range(50)  if is_prime(x)}
print(list3)
print(tupl1)
print(dict1)



