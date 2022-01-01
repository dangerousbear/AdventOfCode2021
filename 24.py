import operator as op
lines = open("24.txt", "r").readlines()
# for line in lines:
#     print(line)
    
def addToDict(k, v, d):
    d[k] = d[k] + v if k in d else v
ops = {"add": op.add, "mul": op.mul, "div": (lambda a,b : a // b), "mod" : (lambda a,b : a % b ), "eql" : (lambda a,b : int(a==b))}



var2Idx = {"x" : 0, "y" : 1, "z" : 2, "w" : 3}


occurenceVar2Deps = []

refSeq = lines[0:18]


xOffsets = []
yOffsets = []
zDivs = []

for i, line in enumerate(lines):
    toks = line.split()
    if i % 18 == 4:
        assert(toks[0] == "div" and toks[1] == "z")
        zDivs.append(int(toks[2]))
    elif i % 18 == 5:
        assert(toks[0] == "add" and toks[1] == "x" and toks[2] != "z")
        xOffsets.append(int(toks[2]))
    elif i % 18 == 15:
        assert(toks[0] == "add" and toks[1] == "y")
        yOffsets.append(int(toks[2]))
    else: assert(line == refSeq[i % 18])


# def forward(i,z,w):
#     return z//zDivs[i] if z % 26 + xOffsets[i] == w else z//zDivs[i] * 26 + yOffsets[i] + w
def forward(i,z,w):
    if z % 26 + xOffsets[i] == w:
        assert(xOffsets[i] < 10)
        return z//zDivs[i]
    return z//zDivs[i] * 26 + yOffsets[i] + w if xOffsets[i] >= 10 else None

costToLevelZ = dict()

def search(z, level, cost, path):
    if (z,level) in costToLevelZ and costToLevelZ[(z,level)][0] > cost:
        return
    costToLevelZ[(z,level)] = cost, path
    # if (level >= 7):
    if (level == len(zDivs)):
        # if cost < 15:
        #     print(path, cost)
        return
    
    for n in range(1,10):
        newZ = forward(level,z,n)
        if newZ != None:
            search(newZ, level + 1, cost + n, path + [n])
    

search(0, 0, 0, [])

for k,v in costToLevelZ.items():
    if k[1] == len(zDivs):
        print(k,v)

# n2ValidZ = [{k : [] for k in range(1,10)} for i in range(len(zDivs))]
# n2ValidZ[13] ={1: [13],
#  2: [14],
#  3: [15],
#  4: [16],
#  5: [17],
#  6: [18],
#  7: [19],
#  8: [20],
#  9: [21]}

# Last 
# for n in range(1, 10):
#     # for x in range(-100, 100):
#     x, y = 0,0
#     startZ = 0
#     for z in range(startZ, searchN):     
#         if forward(len(zDivs)-1, z,n) == 0:
#             # print("Found at N ", n,x,y,z)
#             n2ValidZ[-1][n].append(z)
#             startZ = z
#             break

   
# for i in range(len(zDivs) - 2, -1, -1):
#     print("opSeq number ", i)
#     lastValid = n2ValidZ[i+1]
#     for n in range(1, 10):
#         x, y = 0,0
#         if i == 0:
#             z = 0
#             outZ = forward(i,z,n)
#             if outZ in lastValid[n]:
#                 n2ValidZ[i][n].append(z)
#         else:
#             for validN, validZ in lastValid.items():
#                 for z in inverseX0(i, validZ[0]):
#                     outZ = forward(i,z,n)
#                     for v in lastValid.values():
#                         if outZ in v:
#                             n2ValidZ[i][n].append(z)
#                 for z in inverseX1(i, validZ[0],n): 
#                     outZ = forward(i,z,n)
#                     for v in lastValid.values():
#                         if outZ in v:
#                             n2ValidZ[i][n].append(z)
                
# opSeqs = []
# for i, line in enumerate(lines):
#     toks = line.split()
#     if toks[0] == "inp":
#         opSeqs.append([])
#         foundMulY0 = False
#     else:
#         if lines[i-1].split()[0] == "inp":
#             assert(toks[0] == "mul" and toks[1] == "x" and toks[2] == "0")
#             continue
#         if foundMulY0:
#             opSeqs[-1].append((ops[toks[0]], var2Idx[toks[1]], toks[2] if toks[2] in var2Idx else int(toks[2])))
#         if not foundMulY0 and toks[1] == "y":
#             assert(toks[0] == "mul" and toks[2] == "0")
#             prevToks = lines[i-1].split()
#             prevToks2 = lines[i-2].split()
#             assert(prevToks[0] == "eql" and prevToks[1] == "x" and prevToks[2] == "0")
#             assert(prevToks2[0] == "eql" and prevToks2[1] == "x" and prevToks2[2] == "w")
#             foundMulY0 = True
#         if foundMulY0:
#             assert(toks[0] != "eql" and toks[0] != "mod" and toks[0] != "div" and toks[1] != "x")
#         if toks[0] == "add" and toks[1] == "x" and toks[2] != "z":
#             xOffsets.append(int(toks[2]))
#         if toks[0] == "div" and toks[1] == "z":
#             zDivs.append(int(toks[2]))
# lines.reverse()
# for i, line in enumerate(lines):
#     toks = line.split()
#     if len(toks) == 2:
#         occurenceVar2Deps.append((toks[1], "inp"))
#     else:
#         o = ops[toks[0]]
#         occurenceVar2Deps.append((toks[1], o, toks[2] if toks[2] in var2Idx else int(toks[2])))
# G = dict()

# vLevels = [0] * 4
# for dep in occurenceVar2Deps:
#     sVar = dep[0]
#     vi = var2Idx[sVar]
#     if len(dep) == 2:
#         G[(sVar, vLevels[vi])] = ("inp", "inp")
#     else:
#         rh = dep[2]
#         if rh in var2Idx:
#             G[(sVar, vLevels[vi])] = (dep[1], rh, vLevels[var2Idx[rh]])
#         else:
#             G[(sVar, vLevels[vi])] = (dep[1], rh)
#     vLevels[vi] += 1

# def forward(i,z,w):
#     x = 0 if z % 26 + xOffsets[i] == w else 1
#     v = [x, 0, z//zDivs[i],w]
#     for o, vIdx, v2 in opSeqs[i]:
#         v[vIdx] = o(v[vIdx], v[var2Idx[v2]] if v2 in var2Idx else int(v2))
#     return v[2]


    # for line in lines:
    #     toks = line.split()
    #     if toks[0] == "inp":
    #         v[var2Idx[toks[1]]] = N[nIdx]
    #         nIdx += 1
    #     else:
    #         vIdx = var2Idx[toks[1]]
    #         v2 = toks[2]
    #         o = ops[toks[0]]
    #         v[vIdx] = o(v[vIdx], v[var2Idx[v2]] if v2 in var2Idx else int(v2))
# print(v)


 
 
 
 
    
# for i in range(100000):
#     if i % 5000 == 0:
#         print(N)
    
#     if forward(lines) == 0:
#         print("Found at N ", N)
#         break
    
#     for j in range(len(N) -1, -1, -1):
#         if N[j] < 9:
#             N[j] += 1
#             for k in range(j+1, len(N)):
#                 N[k] = 1
#             break
        
    