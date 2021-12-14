# Setup
def addToDict(k, v, d):
    d[k] = d[k] + v if k in d else v

lines = [line[:-1] for line in open("14.txt", "r").readlines()]
rules = dict()
for line in lines[2:]:
    toks = line.split(" -> ")
    rules[toks[0]] = [toks[0][0] + toks[1],toks[1] + toks[0][1]]
    
nPerPair = dict()
s = lines[0]
for i in range(1, len(s)):
    addToDict(s[i-1] + s[i], 1, nPerPair)

# Count number of pairs
for i in range(40):
    additions = dict()
    for pair in nPerPair:
        for newPair in rules[pair]: addToDict(newPair, nPerPair[pair], additions)
        nPerPair[pair] = 0

    for pair in additions: addToDict(pair, additions[pair], nPerPair)
        
    for p in [pair for pair in nPerPair if nPerPair[pair] <= 0]: del nPerPair[p] #Remove zeroes

# Count number of letters
nPerChar = dict()
for pair in nPerPair:
    addToDict(pair[0], nPerPair[pair], nPerChar)
    addToDict(pair[1], nPerPair[pair], nPerChar)
for c in nPerChar: #Remove doubles
    nPerChar[c] = -(-nPerChar[c] // 2)

print(nPerChar[max(nPerChar, key=nPerChar.get)]  - nPerChar[min(nPerChar, key=nPerChar.get)])


# Slow solution (part 1)
# def evolve(s):
#     newS = ""
#     for i in range(1, len(s)):
#         pair =  s[i-1] + s[i]
#         # print("considering pair " + pair)
       
#         newS += s[i-1] + rules[pair] if pair in rules else s[i-1]
#         # print(newS)
#     # print(newS)
#     return newS + s[-1]

# for n in range(40):
#     s = evolve(s)
#     # print(len(s))
