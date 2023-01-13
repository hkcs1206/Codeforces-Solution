n = int(input())
c = 0
for i in range(n):
    n1 = input()
    if(n1=="Tetrahedron"):
        c+=4
    elif(n1=="Cube"):
        c+=6
    elif(n1=="Octahedron"):
        c+=8
    elif(n1=="Dodecahedron"):
        c+=12
    elif(n1=="Icosahedron"):
        c+=20
print(c)
