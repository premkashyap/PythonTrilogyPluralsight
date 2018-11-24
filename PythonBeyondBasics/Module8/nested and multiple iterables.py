points = [(x,y) for x in range(5) if x%2 ==0 for y in range(5) if y%2 != 0]

pnt = []
for x in range(5):
    if x%2 == 0:
        for y in range(5):
            if y%2 != 0:
                pnt.append((x,y))


triangles = [(x,y) for x in range(5) for y in range(x)]
print(points)
print(pnt)
print(triangles)

nested = [[y*3 for y in range(x) if y !=0] for x in range(5) if x !=0]

outer = []
for x in range(5):
    inner = []
    if x!=0:
        for y in range(x):
            if y != 0:
                inner.append(y*3)
    outer.append(inner)
                
print(nested)