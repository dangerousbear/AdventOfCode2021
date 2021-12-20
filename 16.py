import operator as op
operators = {0 :op.add, 1 : op.mul, 2: (lambda a,b : min(a,b)), 3 : (lambda a,b : max(a,b)), 5: (lambda a,b : int(a > b)), 6 : (lambda a,b : int(a < b)), 7: (lambda a,b : int(a == b))}

s2 = ""
for h in open("16.txt", "r").readlines()[0][:-1]:
    hInt = int(h,16)
    s2 += f'{hInt:0>4b}'
    
def readLiteral(k):
    readBits = ""
    while(s2[k] == '1' and k + 5 < len(s2)):
        readBits += s2[k+1:k+5]
        k+=5
    readBits += s2[k+1:k+5]
    k+=5
    return k, int(readBits,2)

def parsePacket(k):
    k+=3
    typeID = int(s2[k:k+3],2)
    k += 3
    if typeID == 4:
        return readLiteral(k)
    else: #Operator packet
        f = operators[typeID]
        lengthID = s2[k]
        k+=1
        if (lengthID == '0'): #One number
            numBits = int(s2[k:k+15],2)
            k+=15
            startK = k
            v = None
            while(k != startK + numBits):
                assert(k < startK + numBits)
                k, val = parsePacket(k)
                v = (val if v == None else f(v,val))
            return k, v
        else: #Number specified by 15 next bits
            numPackets = int(s2[k:k+11],2)
            k+=11
            v = None
            for i in range(numPackets):
                k, val = parsePacket(k)
                v = val if v == None else f(v,val)
            return k, v
k, v = parsePacket(0)
print("tot " + str(v))