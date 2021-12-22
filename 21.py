import heapq as hq
lines = [line[:-1] for line in open("21test.txt", "r").readlines()]

pos1 = int(lines[0][-1])
pos2 = int(lines[1][-1])

maxScore = 21
nTimesReached = {(0, True, pos1, pos2, 0, 0) : 1}
freq = [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]
def addToDict(k, v, d):
    d[k] = d[k] + v if k in d else v

def sim(p1Turn, p1, p2, score1, score2, n):
    states = set()
    for dieSum, f in freq:
        if p1Turn:
            p1New = (p1 + dieSum) % 10
            score1New = score1 + (p1New if p1New > 0 else 10)
            addToDict((score1New + score2, not p1Turn, p1New, p2, score1New, score2), n * f, nTimesReached)
            states.add((score1New + score2,not p1Turn, p1New, p2, score1New, score2))
        else:
            p2New = (p2 + dieSum) % 10
            score2New = score2 + (p2New if p2New > 0 else 10)
            addToDict((score1 + score2New, not p1Turn, p1, p2New, score1, score2New), n * f, nTimesReached)
            states.add((score1 + score2New,not p1Turn, p1, p2New, score1, score2New))
    return states

statesToConsider = [(0, True, pos1, pos2, 0, 0)]
hq.heapify(statesToConsider)

while True:
    print(len(statesToConsider))
    s = hq.heappop(statesToConsider)
    while len(statesToConsider) >0 and s == statesToConsider[0]:
        hq.heappop(statesToConsider)
    
    if s[4] >= maxScore or s[5] >= maxScore: 
        print("Break")
        break
    newStates = sim(s[1], s[2], s[3], s[4], s[5], nTimesReached[s])
    for ns in newStates:
        hq.heappush(statesToConsider, ns)
    
        
n1Win, n2Win = 0, 0
for s, p1Turn, p1, p2, score1, score2 in nTimesReached:
    if score1 >= maxScore:
        n1Win += nTimesReached[(s, p1Turn, p1, p2, score1, score2)]
    if score2 >= maxScore:
        n2Win += nTimesReached[(s, p1Turn, p1, p2, score1, score2)]
print(max(n1Win, n2Win))
