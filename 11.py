lines = [line[:-1].split("-") for line in open("12.txt", "r").readlines()]
neighbors = dict()
for line in lines:
    n1, n2 = line[0], line[1]
    if n1 not in neighbors:
        neighbors[n1] = set()
    if n2 not in neighbors:
        neighbors[n2] = set()
    neighbors[n1].add(n2)
    neighbors[n2].add(n1)

def search(node, visited, doubleVisitDone):
    visited.append(node)        
    count = 0
    for n in neighbors[node]:
        if n == 'start': continue
        if n == "end": count += 1
        else: 
            vCount = visited.count(n)
            if n.isupper() or vCount == 0:
                count += search(n, visited.copy(), doubleVisitDone)
            elif not doubleVisitDone and vCount < 2:
                count += search(n, visited.copy(), True)
    return count
 
print(search('start', [], False))
