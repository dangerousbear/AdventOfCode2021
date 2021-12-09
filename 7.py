xVec = [int(x) for x in open("7.txt", "r").readlines()[0].split(",")]
    
print(min([sum([abs(x - p) * (abs(x - p) + 1) / 2 for x in xVec]) for p in range(min(xVec), max(xVec) + 1)]))