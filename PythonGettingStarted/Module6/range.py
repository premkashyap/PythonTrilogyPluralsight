print(list(range(5))) #Providing only stop value. Startd from 0 ends at 4. Last element is excluded.
print(list(range(5,10))) #providing start and stop value. Starts at 5 ends at 9. Last element is excluded.
print(list(range(10,20, 3))) #providing start, stop and interval value. Starts at 5 ends at 9. Last element is excluded.

list1 = "Pune Delhi Mumbai Hyderabad Kolkata".split()

for i in enumerate(list1): #returns tuple with item and it's index
    print(i)

for i,v in enumerate(list1): #returns tuple with item and it's index. using with conjuction of tuple unpacking
    print(i, v)