import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
lines = [line[:-1].replace(".","0").replace("#","1") for line in open("20.txt", "r").readlines()]


vals = []
decoder = ""
nSteps = 50

emptyLineFound = False
for line in lines:
    if line == "":
        emptyLineFound = True
    elif emptyLineFound:
        vals.append([int(x) for x in line])
    else:
        decoder += line

v = np.pad(np.array(vals), nSteps)

xs, ys = v.shape
emptyVal = "0"

for n in range(nSteps):
    newV = v.copy()
    for i in range(xs):
        for j in range(ys):
            topRow = emptyVal * 3 if i == 0 else ( (str(v[i-1][j-1]) if j > 0 else emptyVal) + str(v[i-1][j]) + (str(v[i-1][j+1]) if j + 1 < ys else emptyVal))
            midRow = (str(v[i][j-1]) if j > 0 else emptyVal) + str(v[i][j]) + (str(v[i][j+1]) if j + 1 < ys else emptyVal)
            botRow = emptyVal * 3 if i + 1 == xs else ( (str(v[i+1][j-1]) if j > 0 else emptyVal) + str(v[i+1][j]) + (str(v[i+1][j+1]) if j + 1 < ys else emptyVal))
            binStr = topRow + midRow + botRow
            idx = int(binStr,2)
            newV[i][j] = decoder[idx]
    v = newV
    emptyVal = "1" if emptyVal == "0" else "0"

plt.imsave('20.png', v, cmap=cm.gray)
            
print(sum(sum(v)))