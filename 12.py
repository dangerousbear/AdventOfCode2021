vals = [[int(x) for x in line[:-1]] for line in open("11.txt", "r").readlines()]

Ly = len(vals)
Lx = len(vals[0])


def neighbors(i, j):
    hasUp = i > 0
    hasDown = i + 1 < Ly
    hasRight = j + 1 < Lx
    hasLeft = j > 0
    
    if hasUp: 
        yield (i - 1, j)
        if (hasLeft):
            yield (i - 1, j - 1)
        if (hasRight):
            yield (i - 1, j + 1)
    if hasLeft: yield (i, j - 1)
    if hasRight: yield (i, j + 1)
    if hasDown: 
        yield (i + 1, j)
        if (hasLeft):
            yield (i + 1, j - 1)
        if (hasRight):
            yield (i + 1, j + 1)


def flash(vals, i,j):
    if (vals[i][j] == -1): return 0
    vals[i][j] += 1
    if (vals[i][j] < 10): return 0
    #print("Flashing at " + str(i) + " " + str(j))
    vals[i][j] = -1
    count = 1
    for (ni, nj) in neighbors(i,j):
        count += flash(vals, ni, nj)
    return count

flashCount = 0
allZero = False
for n in range(1000):
    
    for i in range(Ly):
        for j in range(Lx):
            vals[i][j] += 1
    
    for i in range(Ly):
        for j in range(Lx):
            val = vals[i][j]
            if val >= 10:
                flashCount += flash(vals, i,j)
    for i in range(Ly):
        for j in range(Lx):
            vals[i][j] = max(vals[i][j], 0)
    allZero = True
    for i in range(Ly):
        for j in range(Lx):
            allZero = allZero and vals[i][j] == 0
    if allZero:
        print(n+1)
        break
            
    print(flashCount)
    
