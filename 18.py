import math
lines = [line[:-1] for line in open("18.txt", "r").readlines()]

def parseInt(s,i, backwards):
    l = 0
    while s[i].isnumeric() and i > 0 and i + 1 < len(s):
        l += 1
        i += 1 if not backwards else -1
    return int(s[i+1:i+l+1] if backwards else s[i-l:i])

def explode(s):
    level = 0
    idxOfComma = -1
    for i, x in enumerate(s):
        # print(x)
        if x == "[":
            level += 1
            # print("Level " + str(level))
            
        elif x == "]":
            level -= 1
            # print("Level " + str(level))
        elif level > 4 and x == "," and s[i-1].isnumeric() and s[i+1].isnumeric():
            idxOfComma = i
            break
    if (idxOfComma == -1):
        return False, s
    
    # print(idxOfComma)
    leftNum = parseInt(s, idxOfComma-1, True)
    rightNum = parseInt(s, idxOfComma+1, False)
    s = s[:idxOfComma-len(str(leftNum)) - 1] + "0" + s[idxOfComma + len(str(rightNum)) + 2:]
    idxOfComma -= 2
    for i in range(idxOfComma+1, len(s)):
        if (s[i].isnumeric()):
            foundInt = parseInt(s, i, False)
            newInt = foundInt + rightNum
            s = s[:i] + str(newInt) + s[i + len(str(foundInt)):]
            break
    for i in range(idxOfComma-2, 0, -1):
        if (s[i].isnumeric()):
            foundInt = parseInt(s, i, True)
            newInt = foundInt + leftNum
            s = s[:i-len(str(foundInt))+1] + str(newInt) + s[i + 1:]
            break
    
    # print(s)
    return True, s

def split(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            xInt = parseInt(s, i, False)
            if xInt >= 10:
                return True, s[:i] + "[" + str(xInt // 2) + "," + str(math.ceil(xInt / 2.0)) + "]" + s[i+len(str(xInt)):] 
    return False, s
     
def tryReduce(s):
    # print("len before "  + str(len(s)))
    changed, s = explode(s)
    if (changed): 
        # print("len after explode "  + str(len(s)))
        return True,s
    # print("split")
    return split(s)


def reduce(s):
    changed = True
    while changed:
        changed, s = tryReduce(s)
        # print(s)
    return s

def add(s1, s2):
    # print("Added")
    return "[" + s1 + "," + s2 + "]"


    # print(s)
# print(s)

def magnitude(x):
    left = x[0] if isinstance(x[0], int) else magnitude(x[0])
    right = x[1] if isinstance(x[1], int) else magnitude(x[1])
    return 3 * left + 2 * right

def recSum(x):
    left = x[0] if isinstance(x[0], int) else recSum(x[0])
    right = x[1] if isinstance(x[1], int) else recSum(x[1])
    return left + right

def isBalanced(s):
    level = 0
    for i, x in enumerate(s):
        if x == "[":
            level += 1
        elif x == "]":
            if (level ==0):return False
            level -= 1
    return level == 0
# print(s)
maxMag = 0

for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            s = reduce(add(lines[i], lines[j]))
            exec("maxMag = max(maxMag,magnitude(" + s + "))")
            print(maxMag)






       