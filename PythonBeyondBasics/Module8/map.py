for i in map(str.capitalize, "The quick brown fox jumps over the lazy dog"):
    print(i)

def sum(x,y,z):
    return x+y+z

X = [2,3,5]
Y = [2,4,8,16]
Z = [1,4,9,16,25]

for i in map(sum, X,Y,Z):
    print(i)