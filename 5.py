f = open("5.txt", "r")
lines = f.readlines()

drawnNumberStrings = lines[0].split(",")
drawnNumbers = []

xStartValues = []
yStartValues = []

xStopValues = []
yStopValues = []

for line in lines:
    tokens = line.split(" -> ")
    assert(len(tokens) == 2)
    startValues = tokens[0].split(",")
    stopValues = tokens[1].split(",")
    assert(len(startValues) == len(stopValues) == 2)
    xStartValues.append(int(startValues[0]))
    yStartValues.append(int(startValues[1]))
    xStopValues.append(int(stopValues[0]))
    yStopValues.append(int(stopValues[1]))


nValues = len(xStartValues)

field = [ [0]*1000 for i in range(1000)]

for i in range(nValues):
    xStart = xStartValues[i]
    xStop = xStopValues[i]
    yStart = yStartValues[i]
    yStop = yStopValues[i]
    
    if (xStart == xStop):
        for y in range(min(yStart, yStop), max(yStart, yStop) + 1):
            field[y][xStart] += 1
    elif (yStart == yStop):
        for x in range(min(xStart, xStop), max(xStart, xStop) + 1):
            field[yStart][x] += 1
    else:
        
        if xStart > xStop:
            xStart, xStop = xStop, xStart
            yStart, yStop = yStop, yStart
        diff = xStop - xStart
        assert(abs(yStop - yStart) == diff) #Assert diagonal
        yIncrementSign = 1 if yStop > yStart else -1
        for k in range(diff + 1):
            field[yStart + yIncrementSign * k][xStart + k] += 1
        
        #print(xStart)
        #print(xStop)
        #print(yStart)
        #print(yStop)
        #assert(False)

def between(x, y, z):
    return x <= y and y <= z

numValsGreaterThanOne = 0
# for i in range(1000):
#     for j in range(1000):
#         nCrossings = 0
#         for k in range(nValues):
#             xStart = xStartValues[k]
#             xStop = xStopValues[k]
#             yStart = yStartValues[k]
#             yStop = yStopValues[k]
            
#             nCrossings += 1 if (xStart == xStop or yStart == yStop) and between(xStart, i, xStop) and between(yStart, j, yStop) else 0
#             if (nCrossings > 1):
#                 numValsGreaterThanOne += 1
#                 break
                
        

for line in field:
    for val in line:
        if (val > 1):
            numValsGreaterThanOne += 1

print(numValsGreaterThanOne)