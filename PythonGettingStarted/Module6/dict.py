dict1 = {'prem':'kashyap', 'anita':'gautam'}
dict2 = [('Prem', 'Kashyap'),('Anita', 'Gautam')]
dict3 = dict(prem='kashyap', anita = 'gautam')
dict4 = dict1.copy() #2 methods of shallow copying the dictionary
dict5 = dict(dict2)
dict1.update({'anil':'kaushik', 'pawan':'mourya'})
print(dict1)
for d in dict1:
    print(d, dict1[d])
print('*'*20)
for d in dict1.keys(): #redundant as defualt iterations returns key
    print(d)
print('*'*20)
for d in dict1.values():
    print(d)
print('*'*20)
for k,v in dict1.items():
    print(k,' : ',v)

print('prem' in dict1) #only for keys.

del dic1['pawan'] #only for keys