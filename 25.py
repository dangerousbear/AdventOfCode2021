import copy
F = [[int(x) for x in line.replace(">","1").replace("v", "2").replace(".","0").replace("\n","")] for line in open("25.txt", "r").readlines()]




Ly = len(F)
Lx = len(F[0])


def rightNbor(i,j):
    return j + 1 if j + 1 < Lx else 0
def botNbor(i,j):
    return i + 1 if i + 1 < Ly else 0

for n in range(1000):
    indicesToMove = []
    
    for i in range(Ly):
        for j in range(Lx):
           f = F[i][j]
           if f == 1 and F[i][rightNbor(i,j)] == 0:
               indicesToMove.append((i,j))
    
    for i,j in indicesToMove:
        F[i][j] = 0
        F[i][rightNbor(i,j)] = 1
        
    indicesToMove2 = []
    
    for i in range(Ly):
        for j in range(Lx):
           f = F[i][j]
           if f == 2 and F[botNbor(i,j)][j] == 0:
               indicesToMove2.append((i,j))
    
    for i,j in indicesToMove2:
        F[i][j] = 0
        F[botNbor(i,j)][j] = 2
        
    if len(indicesToMove) == 0 and len(indicesToMove2) == 0:
        print(n + 1)
        break
        
