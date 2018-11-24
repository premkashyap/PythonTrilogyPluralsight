set1 = {1,5,9,3434}
set2 = {} #empty dictionary
set3 = set() #empty set
set4 = {1,2,2,5} #dupes are discarded

set4.add(6)
set4.add(5) #discarded
set4.update([45,67,12])
set4.discard(2)
#set4.remove(2) #gives key error if the key is not present in set

male = {"prem", "pawan", "vicky", "raghu"}
maths = {"prem", "raghu", "monali", "aakankasha"}
bio = {"pawan", "anita", "mona"}
female = {"anita", "monali", "mona", "aakankasha", "shweta"}
male_engineer = male.intersection(maths)
female_medical = female.intersection(bio)
student = male.union(female).union(bio).union(maths)
female_nostream = female.difference(maths).difference(bio)
female_or_bio = female.symmetric_difference(bio)
print(student.issuperset(male))
print(bio.issubset(student))
print(male.isdisjoint(female))