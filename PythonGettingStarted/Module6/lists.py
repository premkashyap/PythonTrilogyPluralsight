list1 = "Pune Delhi Mumbai Hyderabad Kolkata".split()
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list1.sort(key=len)
print(list1)
print(reversed(list1)) # for getting a reveresed collection fo an existing collection without modifying it
print(sorted(list1)) # for getting a reveresed iterable fo an existing collection without modifying it.
print(list1[0])
print(list1[-1]) #reverse indexing. starts from end. endmost is -1 and decreses by 1 going leftwards.
print(list1[-4])
print(list1[1:3])
print(list1[1:-1])
list1 = list1[:] #3 ways of shallow copying a list
list2 = list1.copy()
list3 = list(list1)
list4 = list1*2
print(list4)

list5 = [[-1, 1]]*5
print(list5)
list5[3].append(100)
print(list5)  #trap

stringList = "The quick brown fox jumps over the lazy dog".split()
print(stringList.index('brown'))
#print(stringList.index('Unicorn')) #Will give exception
print(stringList.count('unicorn'))
print( 'fox' in stringList)

del stringList[1]
stringList.remove('lazy')
stringList.insert(1, 'agile')
print(stringList)
