letterOrder = open("23.txt", "r").read().replace("\n", "").replace(".","").replace("#", "").replace(" ","")
L = 11

startConfig = ()
for c in ["A", "B", "C", "D"]:
    startConfig += tuple(sorted([L+i for i,x in enumerate(letterOrder) if x == c]))

allowedUpperPositions = [0,1,3,5,7,9,10]

def getStepsUp(pos):
        if pos >= L:
            if pos < L + 4:
                return 1
            elif pos < L + 8:
                return 2
            elif pos < L + 12:
                return 3        
            return 4
        return 0


def genMoves(p):
    moves = []
    freeTokens = [i for i, tok in enumerate(p) if (tok < L+4 or tok-4 not in p)]
    for i in freeTokens:
        ri = i // 4
        goalPos0 = L + ri
        goalPos1 = goalPos0 + 4
        goalPos2 = goalPos1 + 4
        goalPos3 = goalPos2 + 4
        
        #Check if goals are filled
        g1 = goalPos1 in p
        g2 = goalPos2 in p
        g3 = goalPos3 in p
        c1 = g1 and p.index(goalPos1) // 4 == ri
        c2 = g2 and p.index(goalPos2) // 4 == ri
        c3 = g3 and p.index(goalPos3) // 4 == ri
        
        if (p[i] == goalPos3 or p[i] == goalPos2 and c3
            or (p[i] == goalPos1 and c2 and c3)
            or (p[i] == goalPos0 and  c1 and c2 and c3)):
            continue
        c = 10**(i // 4)
        
        stepsUp = getStepsUp(p[i])

        #Logic:
        # If free upper position, add move
        # If free goal position and lower goal positions are correct, add move
        # If collision, break
        
        def addMoves(k, accCost):
            if not stepsUp == 0 and k in allowedUpperPositions:
                moves.append((i, k, accCost))
            if k == (goalPos0 - L + 1) * 2 and goalPos0 not in p: # Create move for the appropriate depth
                if not g3:
                    moves.append((i, goalPos3, accCost + 4*c))
                elif c3:
                    if not g2:
                        moves.append((i, goalPos2, accCost + 3*c))
                    elif c2:
                        if not g1:
                            moves.append((i, goalPos1, accCost + 2*c))
                        elif c1:
                            moves.append((i, goalPos0, accCost + c))
        
        startPos = p[i] if stepsUp == 0 else (p[i] - (stepsUp - 1) * 4 - L + 1) * 2 
        k = startPos
        accCost = c * stepsUp
        while(k < L):
            k+=1
            accCost += c
            if k in p:
                break
            addMoves(k,accCost)

                
        k = startPos
        accCost = c * stepsUp
        while(k > 0):
            k-=1
            accCost += c
            if k in p:
                break
            addMoves(k,accCost)
    for m in moves:
        if m[1] > L:
            return [m] # If we can move to burrow, discard other moves (will be re-generated in next step)
    return moves
               
                
        
costMap = dict()
def search(p, cost):
    if p in costMap and costMap[p] <= cost:
        return
    costMap[p] = cost
    for i, pos, c in genMoves(p):
        nBors = list(p[4*(i // 4):(4 + 4*(i // 4))])
        nBors[i % 4] = pos
        pNew = p[:4*(i // 4)] + tuple(sorted(nBors)) + p[(4 + 4*(i // 4)):]

        search(pNew, cost + c)


search(startConfig, 0)

print(costMap[(11, 15, 19, 23, 12, 16, 20, 24, 13, 17, 21, 25, 14, 18, 22, 26)])
