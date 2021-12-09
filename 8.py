lines = open("8.txt", "r").readlines()
values = [[], []]
for line in lines:
    tokens = line.split(" | ")
    values[0].append([set(digit) for digit in tokens[0].split()])
    values[1].append([set(digit) for digit in tokens[1].split()])

def getDigitCodes(tenDigits): # Returns the code corresponding to 0, 1, ... 9
    S = sorted(tenDigits, key=len)
    a = S[1] - S[0] # Top segment is difference between 7 and 1
    posOf6 = [i for i in range(6, 9) if not S[0].issubset(S[i])][0] # Only one six-segment digit, 6, intersects 1 in one place. 0 and 9 intersects in two.
    c = S[0].difference(S[posOf6]) # Top right = Difference of 1 & 6
    posOf09 = list(set([6, 7,8]) - set([posOf6]))
    de = S[posOf09[0]].symmetric_difference(S[posOf09[1]]) # symdiff of 0 & 9 = mid & bot left
    d = de.intersection(S[2])
    e = de - d
    f = S[1] - a - c # Bot right segment is 4 - top - top right
    b = S[2] - d - c - f
    g = S[-1] - a - b - c - d - e - f
    return [set().union(*[a, b, c, e, f, g]),
            set().union(*[c,f]),
            set().union(*[a, c, d, e, g]),
            set().union(*[a, c, d, f, g]),
            set().union(*[b, c, d, f]),
            set().union(*[a, b, d, f, g]),
            set().union(*[a, b, d, e, f, g]),
            set().union(*[a, c, f ]),
            set().union(*[a, b, c, d, e, f, g]),
            set().union(*[a, b, c, d, f, g])]
    
count = 0
for i in range(len(values[0])):    #### Main solution
    digitCodes = getDigitCodes(values[0][i])
    s = ""
    for digit in values[1][i]:
        s += str(digitCodes.index(digit))
    count += int(s)

print(count)


