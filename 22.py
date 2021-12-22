from dataclasses import dataclass
lines = [line[:-1] for line in open("22.txt", "r").readlines()]

onOff = []
xLims = []
yLims = []
zLims = []

for line in lines:
    onOff.append(True if line[1] == "n" else False)
    toks = line[line.index("x"):].split(",")
    xLims.append([int(x) for x in toks[0][2:].split("..")])
    yLims.append([int(y) for y in toks[1][2:].split("..")])
    zLims.append([int(z) for z in toks[2][2:].split("..")])

@dataclass(frozen=True, eq=True)
class Box:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    
    # def intersects(self, c):
    #     return (c.x2 > self.x1 or c.x1 > self.x2 and c.y2 > self.y1 or c.y1 > self.y2 and c.z2 > self.z1 or c.z1 > self.z2
    
    def contains(self, c):
        xContains = c.x1 >= self.x1 and c.x2 <= self.x2
        yContains = c.y1 >= self.y1 and c.y2 <= self.y2
        zContains = c.z1 >= self.z1 and c.z2 <= self.z2
        return xContains and yContains and zContains
    
    def getIntersectionBox(self, c):
        xL = max(self.x1, c.x1)
        xR = min(self.x2, c.x2)
        yL = max(self.y1, c.y1)
        yR = min(self.y2, c.y2)
        zL = max(self.z1, c.z1)
        zR = min(self.z2, c.z2)
        return None if xL > xR or yL > yR or zL > zR else Box(xL, xR, yL, yR, zL, zR)
    
    def volume(self):
        return (self.x2 - self.x1 + 1)*(self.y2 - self.y1 + 1)*(self.z2 - self.z1 + 1)
def addToDict(k, v, d):
    d[k] = d[k] + v if k in d else v

box2Weight = dict()
for i in range(len(onOff)):
    print("i ", i)
    newBox = Box(xLims[i][0], xLims[i][1], yLims[i][0], yLims[i][1], zLims[i][0], zLims[i][1])
    weight = 1 if onOff[i] else -1
    
    intersections = []
    iWeights = []
    for b in box2Weight:
        intersection = newBox.getIntersectionBox(b)
        if intersection is not None:
            intersections.append(intersection)
            iWeights.append(-1 if box2Weight[b] > 0 else 1)

            
    for i, b in enumerate(intersections):
        addToDict(b, iWeights[i], box2Weight)
    
    if (weight > 0):
        addToDict(newBox, weight, box2Weight)
    
    box2Weight = {x:y for x,y in box2Weight.items() if y != 0}
    
volume = 0
for b in box2Weight:
    volume += box2Weight[b] * b.volume()
print(volume)