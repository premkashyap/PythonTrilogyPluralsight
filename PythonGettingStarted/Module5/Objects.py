num1 = 4
num2 = 4
print("*"*20)
print(num1 == num2)  #True as == compares Values
print(num1 is num2)  #True as ints are immutable. Hence both are same objects
print(id(num1))
print(id(num2))
print("*"*20)

list1 = [1,"prem",3]
list2 = [1,"prem",3]

print(list1[0] == list1[0])
print(list1[0] is list2[0])
print(list1[1] == list1[1])
print(list1[1] is list2[1])
print(list1 == list2)  #True as == compares Values
print(list1 is list2)  #False as list are mutable and hence both are different objects
list3 = list1
list3[0]= 10
print("*"*20)
print(list1)
print(list2)
print(list3)
print("*"*20)


def transformmutable(x):
   x[0]= 10
   x[1]= 20
   x[2]= 30
   print(x)

def transformmutable_without_sideaffects(x):
    x = [100, 200, 300]
    print(x)

f = [1,2,3]
print(f)
transformmutable(f)
print(f)
transformmutable_without_sideaffects(f)
print(f)