list_of_peeps = ["Prem Kashyap", "Anita Gautam", "Raghu Rathod"]
print(sorted(list_of_peeps, key = lambda name: name.split()[-1]))

lam = lambda name: name.split()[-1]
print(type(lam))
print(lam("Prem Kozikode"))