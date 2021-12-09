vals = [[int(x) for x in line[:-1]] for line in open("9.txt", "r").readlines()]
Ly = len(vals)
Lx = len(vals[0])


lowPoints = set()

for i in range(Ly):
    for j in range(Lx):
        val = vals[i][j]
        top = i == 0 or val < vals[i-1][j] 
        bot = i + 1 == Ly or val < vals[i+1][j]
        left = j == 0 or val < vals[i][j-1]
        right = j + 1 == Lx or val < vals[i][j+1]
        if top and bot and left and right:
            lowPoints.add((i,j))

def getBasin(i, j):
    top =  vals[i-1][j] if i > 0 else 9 
    bot =  vals[i+1][j] if i + 1 < Ly else 9
    left = vals[i][j-1] if j > 0 else 9
    right = vals[i][j+1] if j + 1 < Lx else 9
    
    
    basin = set([(i,j)])
    val = vals[i][j]
    if top != 9 and val < top:
        basin = basin.union(getBasin(i-1,j))
    if bot != 9 and val < bot:
        basin = basin.union(getBasin(i+1,j))
    if left != 9 and val < left:
        basin = basin.union(getBasin(i,j-1))
    if right != 9 and val < right:
        basin = basin.union(getBasin(i,j+1))
    return basin
        
basinLengths = sorted([len(getBasin(i,j)) for i, j in lowPoints])
print(basinLengths[-1] * basinLengths[-2] * basinLengths[-3])






# for i in range(Ly):
#     for j in range(Lx):
#         val = vals[i][j]
        
#         top = i == 0 or val < vals[i-1][j] 
#         bot = i + 1 == Ly or val < vals[i+1][j]
#         left = j == 0 or val < vals[i][j-1]
#         right = j + 1 == Lx or val < vals[i][j+1]
#         if top and bot and left and right:
#             #print(str(i) + " " + str(j) + " " + str(val))
#             count += val + 1

# print(count)