lines = [line[:-1] for line in open("19.txt", "r").readlines()]

def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    rots = []
    for cycle in range(2):
        for step in range(3):
            v = roll(v)
            rots.append(v)
            for i in range(3):
                v = turn(v)
                rots.append(v)
        v = roll(turn(roll(v)))
    return rots

def get2RotationIdx(i1, i2):
    s = sequence((1,2,3))
    s1 = s[i1]
    s2 = sequence(s1)[i2]
    return s.index(s2)

pts, diffs, indexPairs = [], [], []

for line in lines:
    if ("scanner" in line):
        pts.append([])
        diffs.append([])
        indexPairs.append([])
    elif line != "":
        vals = line.split(",")
        pts[-1].append((int(vals[0]), int(vals[1]), int(vals[2]) if len(vals) > 2 else 0))

for si, pa in enumerate(pts):
    for i, (x0, y0, z0) in enumerate(pa):
        for j in range(i+1, len(pa)):
                # print(i,j)
                x1, y1, z1 = pa[j]
                diffs[si].append((x1 - x0, y1 - y0, z1 - z0))
                indexPairs[si].append((i,j))


scannerPositions = {0 : (0,0,0)}
scannerRotIndices = {0: 11}
unknownScanners = set(range(1, len(pts)))

def getInvRotIdx(i):
    permuted = sequence((1,2,3))[i]
    for j, k in enumerate(sequence(permuted)):
        if k == (1, 2, 3):
            return j
    
pairsConsidered = set()
while len(unknownScanners) > 0:
    foundMatch = False
    for ks in scannerPositions:
        for us in unknownScanners:
            if (ks, us) in pairsConsidered:
                continue
            pairsConsidered.add((ks, us))
            diffsPerRot = []
            for i in range(24):
                diffsPerRot.append([])
                
            print("considering pair " + str(ks) + ", " + str(us))
            for di0, d0 in enumerate(diffs[ks]):
                rots = sequence(d0)
                for di1, (d1x, d1y, d1z) in enumerate(diffs[us]):
                    for rotIdx, (px, py, pz) in enumerate(rots):
                        if (d1x, d1y, d1z) == (px, py, pz):
                            diffsPerRot[rotIdx].append((indexPairs[ks][di0], indexPairs[us][di1]))
                        elif (d1x, d1y, d1z) == (-px, -py, -pz):
                            p1, p2 = indexPairs[ks][di0]
                            diffsPerRot[rotIdx].append(((p2, p1), indexPairs[us][di1]))
                            
            maxMatches = max(diffsPerRot, key=len)
            if len(maxMatches) >= 66:
                rotIdx = diffsPerRot.index(maxMatches)
                
                srcScannerRotIdx = scannerRotIndices[ks]
                
                scannerRotIndices[us] = get2RotationIdx(srcScannerRotIdx, rotIdx)
                invRotIdx = getInvRotIdx(rotIdx)
                pPair1, pPair2 = maxMatches[0]
                ptk1, ptk2 = pPair1
                ptu1, ptu2 = pPair2
                xk, yk, zk= pts[ks][ptk1]
                xu, yu, zu = sequence(pts[us][ptu1])[invRotIdx]
                shiftFound = xk - xu, yk - yu , zk - zu 
                sx, sy, sz = sequence(shiftFound)[getInvRotIdx(srcScannerRotIdx)]
                ksx, ksy, ksz = scannerPositions[ks]
                scannerPositions[us] = (ksx + sx, ksy + sy, ksz + sz) 
                unknownScanners.remove(us)
                foundMatch = True
                break
        if foundMatch:
            break
                
maxD = 0
for si1 in scannerPositions:
    sp1 = scannerPositions[si1]
    for si2 in scannerPositions:
        sp2 = scannerPositions[si2]
        d = abs(sp1[0] - sp2[0]) + abs(sp1[1] - sp2[1]) + abs(sp1[2] - sp2[2])
        maxD = max(d, maxD)

print(maxD)
                            


