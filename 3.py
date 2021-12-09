def filter(lines, bitPos, keepMostCommon):
    numZeros = 0
    numOnes = 0
    
    
    for line in lines:
        bit = int(line[bitPos])
        if (bit == 0):
            numZeros += 1
        elif (bit == 1):
            numOnes += 1
        else:
            assert(False)
    
    bitToKeep = "0"
    if (keepMostCommon):
        bitToKeep = "1" if (numOnes >= numZeros) else "0"
    else:
        bitToKeep = "1" if (numOnes < numZeros) else "0"
    lines[:] = [line for line in lines if line[bitPos] == bitToKeep]
    

f = open("3.txt", "r")
lines = f.readlines()


# first reading
bitPos = 0
while (len(lines) > 1):
    filter(lines, bitPos, True)
    bitPos += 1
    print(len(lines))

assert(len(lines) == 1)
print (lines[0])

print(int(lines[0], 2))

f = open("3.txt", "r")
lines = f.readlines()


# second reading
bitPos = 0
while (len(lines) > 1):
    filter(lines, bitPos, False)
    bitPos += 1
    print(len(lines))

assert(len(lines) == 1)
print (lines[0])

print(int(lines[0], 2))