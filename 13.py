import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
lines = [line[:-1] for line in open("13.txt", "r").readlines()]

pts = set()
folds = []
emptyLineFound = False
for line in lines:
    if emptyLineFound:
        i = line.index('=')
        folds.append((line[i-1] == 'x', int(line[i+1:])))
    elif line == '':
        emptyLineFound = True
    else:
        tokens = line.split(',')
        x, y = int(tokens[0]), int(tokens[1])
        pts.add((x,y))

def fold(pts, foldCoord, isX):
    newPts = set()
    for (x, y) in pts:
        if isX:
            assert(x != foldCoord)
            newPts.add( (x,y) if x < foldCoord else (2*foldCoord - x, y) )
        else:
            assert(y != foldCoord)
            newPts.add( (x,y) if y < foldCoord else (x, 2*foldCoord - y) )
    return newPts

for (isX, coord) in folds:
    pts = fold(pts, coord, isX)
# Get image
xs, ys = 0, 0
for x,y in pts:
    xs = max(xs, x + 1)
    ys = max(ys, y + 1)

field = np.zeros((xs, ys), dtype=int)
for x, y in pts:
    field[x,y] = 1
plt.imsave('13.png', np.flipud(field), cmap=cm.gray)

