string = "New Delhi"
print('length using len function: ', len(string))
joined_string = string + "Mumbai" + "Tokyo" # supports + operator but method is inefficient leading to lot of memory wastage
joined_string += 'Hubbali'
print(joined_string)
joined_string = ' '.join(['Delhi', 'Mumbai', 'Kolkata']) #passing an iterable to join method called by an empty string. The strig that has called is used as a joiner.
print(joined_string)
joined_string_with_joiner = ';'.join(['Delhi', 'Mumbai', 'Kolkata'])
print(joined_string_with_joiner)

departure, separator, arrival = "London:Amsterdam".partition(':') #partition partiions a string in 3 parts, a seaprator, before the seaprtor and after the seaprator. return tuple
print(departure, separator, arrival)
departure, _, arrival = "London:Amsterdam".partition(':') #to ignore the separtor. _ is ignored as a convention. Though not a rule
print(_)
print("The age of {} is {}".format('Anita', 24))
print("The age of {0} is {1}. {0} is married".format('Anita', 24))
print("Latitude of Hyderabad: {Latitude}. Longitude of Hyderabad: {Longitude}".format(Longitude='60E', Latitude='24N',))
position = (10,20,30)
print("Co-ordinates are x:{pos[0]}, y:{pos[1]}, z:{pos[2]}".format(pos= position))
import math
print("Maths Constants: pi={m.pi:.3f} and e = {m.e:.3f}".format(m=math))