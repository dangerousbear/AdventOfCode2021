f = open("4.txt", "r")
lines = f.readlines()

drawnNumberStrings = lines[0].split(",")
drawnNumbers = []

for ns in drawnNumberStrings:
    drawnNumbers.append(int(ns))
    
def hasBingo(indices):
    numTrailingValues = 0
    lastValue = -10
    numOfEachMod = [0] * 5
    for i in indices:
        numOfEachMod[i % 5] += 1
        
        if (lastValue + 1 == i):
            numTrailingValues += 1
            if (numTrailingValues == 5 and i % 5 == 4):
                return True
        else:
            numTrailingValues = 0
        lastValue = i
    
    return max(numOfEachMod) >= 5

L = 5 # Side length

bingoTiles = []
for i in range(1, len(lines)):
    line = lines[i]
    assert(len(line) > 0)
    if (len(line) == 1):
        bingoTiles.append([])
    else:
        for token in line.split():
            bingoTiles[-1].append(int(token))

indicesOfMarkedTiles = []

nTiles = len(bingoTiles)
for tile in bingoTiles:
    assert(len(tile) == L * L)
    indicesOfMarkedTiles.append([])

lastNumber = -1
numBingos = 0
for n in drawnNumbers:
    if (len(bingoTiles) == 0):
        break
    print(len(bingoTiles))
    for i in range(len(bingoTiles)):
        if (i >= len(bingoTiles)):
            break
        tile = bingoTiles[i]
        try:
            indicesOfMarkedTiles[i].append(tile.index(n))
            indicesOfMarkedTiles[i].sort()
        except ValueError:
            pass
        if (hasBingo(indicesOfMarkedTiles[i])):
            numBingos += 1
            if (len(bingoTiles) == 1):
                lastNumber = n
                winTile = bingoTiles[0]
                winMarkedIndices = indicesOfMarkedTiles[0]
                
            bingoTiles.remove(tile)
            indicesOfMarkedTiles.remove(indicesOfMarkedTiles[i])
            
            
print("nBingos " + str(numBingos))
assert(len(bingoTiles) == 0)
assert(len(indicesOfMarkedTiles) == 0)


winSum = 0
totalSum = 0
for i in range(len(winTile)):
    val = winTile[i]
    if i not in winMarkedIndices:
        winSum += val
    totalSum += val


print(totalSum)
print(winSum)
print(lastNumber)
print(lastNumber * winSum)
    
