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


open_list = ["(", "[","{", "<"]
close_list = [")","]","}", ">"]
  
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0 and open_list[pos] == stack[-1]):
                stack.pop()
            else:
                return i
        else:
            assert(False)
    return ""
    # if len(stack) == 0:
    #     return "Balanced"
    # else:
    #     return "Unbalanced"
def check2(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0 and open_list[pos] == stack[-1]):
                stack.pop()
            else:
                assert(False)
        else:
            assert(False)
    return stack
fLines = [line for line in lines if check(line) == ""]


suffixScores = [1, 2, 3, 4]
scores =[]
for line in fLines:
    stack = check2(line)
    sScore = 0
    for c in reversed(stack):
        sScore *= 5
        sScore += suffixScores[charToIdx[c]]
        #print(sScore)
    scores.append(sScore)
scores = sorted(scores)
print(scores[int(len(scores) / 2)])



    
# for lineIdx, line in enumerate(lines):
#     nOpenBrackets = [0] * 4
#     pLastOpen = [-1] * 4
#     for cIdx, c in enumerate(line):
#         i = charToIdx[c]
#         if (isRightChar(c)):
#             if (nOpenBrackets[i] <= 0 or nOpenBrackets[i] == 1 and smallerThanAny(pLastOpen, i)):
#                 print("Found error at line " + str(lineIdx) + " pos "  + str(cIdx) + ", char " + c)
#                 score += scores[i]
#                 break
#             nOpenBrackets[i] -= 1
#         else:
#             pLastOpen[i] = cIdx
#             nOpenBrackets[i] += 1
        
