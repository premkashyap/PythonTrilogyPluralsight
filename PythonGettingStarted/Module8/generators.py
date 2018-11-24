def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()

print(next(g))
print(next(g))
print(next(g))

for i in gen123():
    print(i)

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter +=1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

for item in take(3, [11,21,3,74,15,6]):
    print(item)
for item in distinct([1,2,5,2,7,5,17]):
    print(item)

for item in take(3, distinct([1,2,5,2,7,5,17])):
    print(item)