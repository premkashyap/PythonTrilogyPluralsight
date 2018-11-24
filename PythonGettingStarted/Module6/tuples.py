tup = () #Empty
print(type(tup))
tup = (123) #Not a single element tuples. as () is treated as mathematical operator
print(type(tup))
tup = (123,) #single element tuple
print(type(tup))
tup = (123, 'abc', ('prem', 'kashyap')) #multiple element tuple with nested tuple
print(tup[0], type(tup[0]))
print(tup[1], type(tup[1]))
print(tup[2], type(tup[2]))
tup = tuple(['delhi','mumbai']) #tuples from iterables using tuple constructor
tuptup = tup*2 #tuples support multiplication operator
print('len tup: ', len(tup), ' len tuptup: ', len(tuptup))
(a, b,(c,d)) = (1,2,(3,4)) #Tuple unpacking
print(a)
print(b)
print(c)
print(d)
tup = (1, 2,3,4,5 ,6,7, 8)
print(2 in tup) #containment operator
print(10 not in tup)
for i in tup:
    print(i)

def maxmin(tup):
    return max(tup), min(tup) #returning multiples values from function

max, min = maxmin(tup)
print('max: ', max, 'min: ', min)

tup[0] = 10 #once initialized tuples cant be changed. They are immutable.