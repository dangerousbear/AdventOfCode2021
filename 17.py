import math
line = open("17.txt", "r").readlines()[0][:-1]
subStr = line[line.index("x="):]
toks = subStr.split(", ")
xLimStrs = toks[0][2:].split("..")
xLims = [int(x) for x in xLimStrs]
yLimStrs = toks[1][2:].split("..")
yLims = [int(y) for y in yLimStrs]
    
def between(x,y,z):
    return x <= y and y <= z
def xN(v0, N):
    return N * v0 - (N-1)*N//2

def NfromX(v0, xTar, positiveRoot):
    p = v0 + 0.5
    d = p*p - 2.0*xTar
    if d < 0: return 1000
    return p + math.sqrt(d) if positiveRoot else p - math.sqrt(d)

def forwardSim(xv,yv):
    x, y = 0,0
    n = 0
    # yMax = -100000
    while True:
        if between(xLims[0], x, xLims[1]) and between(yLims[0], y, yLims[1]):
            return True
        if x > xLims[1] or y < yLims[0]:
            return False
        n += 1
        x+=xv
        y+=yv
        xv += 0 if xv == 0 else (1 if xv < 0 else -1)
        yv -= 1
    
        


N = 0
for xv0 in range(2, 500):
    for yv0 in range(-144, 5000):
        NyLower = math.floor(NfromX(yv0, yLims[1], True))
        NyUpper = math.ceil(NfromX(yv0, yLims[0], True))
        NxLower = math.floor(NfromX(xv0, xLims[0], False))
        NxUpper = math.ceil(NfromX(xv0, xLims[1], False))
        minN = max(NyLower, NxLower)
        maxN = min(NyUpper, NxUpper)
        if maxN >= minN and forwardSim(xv0, yv0):
            N += 1
print(N)             

    