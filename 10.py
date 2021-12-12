lines = [line[:-1] for line in open("10.txt", "r").readlines()]

scores = [3, 57, 1197, 25137]

charToIdx = {
    "(" : 0,
    ")" : 0,
    "[" : 1,
    "]" : 1,
    "{" : 2,
    "}" : 2,
    "<" : 3,
    ">" : 3
}

def isRightChar(c):
    return c == ")" or c == "]" or c == "}" or c == ">"

def smallerThanAny(pLastOpen, k):
    for i, val in enumerate(pLastOpen):
        if (val >= 0 and val < pLastOpen[k]):
            return True
    return False


leftSymbols = ["(", "[","{", "<"]
rightSymbols = [")","]","}", ">"]
  
def check(myStr):
    stack = []
    for i in myStr:
        if i in leftSymbols:
            stack.append(i)
        elif i in rightSymbols:
            pos = rightSymbols.index(i)
            if (len(stack) > 0 and leftSymbols[pos] == stack[-1]):
                stack.pop()
            else:
                return i
        else:
            assert(False)
    return stack

fLines = [line for line in lines if isinstance(check(line), list)]


suffixScores = [1, 2, 3, 4]
scores =[]
for line in fLines:
    stack = check(line)
    sScore = 0
    for c in reversed(stack):
        sScore *= 5
        sScore += suffixScores[charToIdx[c]]
        #print(sScore)
    scores.append(sScore)
scores = sorted(scores)
print(scores[int(len(scores) / 2)])


