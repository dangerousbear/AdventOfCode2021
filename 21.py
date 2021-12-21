lines = [line[:-1] for line in open("21.txt", "r").readlines()]

pos1 = int(lines[0][-1])
pos2 = int(lines[1][-1])

maxScore = 21
nTimesReached = {(True, pos1, pos2, 0, 0) : 1}
freq = [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]
def addToDict(k, v, d):
    d[k] = d[k] + v if k in d else v

def sim(p1Turn, p1, p2, score1, score2, n):
    states = set()
    for dieSum, f in freq:
        if p1Turn:
            p1New = (p1 + dieSum) % 10
            score1New = score1 + (p1New if p1New > 0 else 10)
            addToDict((not p1Turn, p1New, p2, score1New, score2), n * f, nTimesReached)
            states.add((not p1Turn, p1New, p2, score1New, score2))
        else:
            p2New = (p2 + dieSum) % 10
            score2New = score2 + (p2New if p2New > 0 else 10)
            addToDict((not p1Turn, p1, p2New, score1, score2New), n * f, nTimesReached)
            states.add((not p1Turn, p1, p2New, score1, score2New))
    return states
 
statesToConsider = set([(True, pos1, pos2, 0, 0)])

while True:
    minScoreSumState = (True, pos1, pos2, maxScore, maxScore)
    for s in statesToConsider:
        if s[3] + s[4] < minScoreSumState[3] + minScoreSumState[4] and s[3] < maxScore and s[4] < maxScore:
            minScoreSumState = s
    
    if minScoreSumState[3] >= maxScore or minScoreSumState[4] >= maxScore: 
        print("break")
        break
    statesToConsider.update(sim(*(minScoreSumState + (nTimesReached[minScoreSumState],))))
    statesToConsider.remove(minScoreSumState)
    
        
n1Win = 0
n2Win = 0
n1Wins = []
for p1Turn, p1, p2, score1, score2 in nTimesReached:
    if score1 >= maxScore:
        assert(score2 < maxScore)
        n1Win += nTimesReached[(p1Turn, p1, p2, score1, score2)]
        n1Wins.append(nTimesReached[(p1Turn, p1, p2, score1, score2)])
    if score2 >= maxScore:
        assert(score1 < maxScore)
        n2Win += nTimesReached[(p1Turn, p1, p2, score1, score2)]
print(n1Win // 2)
print(n2Win // 2)
