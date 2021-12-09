hist = [0] * 9
for nStr in open("6test.txt", "r").readlines()[0].split(","):
    hist[int(nStr)] += 1
    
for i in range(256):
    firstVal = hist.pop(0)
    hist[6] += firstVal
    hist.append(firstVal)
print(sum(hist))

# for i in range(256):
#     newHist = [0] * 9
#     for i in range(9):
#         newHist[i] = hist[i+1] if i < 8 else hist[0]
#     newHist[6] += hist[0]
#     hist = newHist


    

# timers = []
# for nStr in lines[0].split(","):
#     timers.append(int(nStr))
    
# def advanceOneGeneration(timers):
#     numNewFish = 0
#     for i in range(len(timers)):
#         if timers[i] == 0:
#             timers[i] = 6
#             numNewFish += 1
#         else:
#             timers[i] -= 1
#     timers.extend([8] * numNewFish)



# print(timers)
# for i in range(256):
#     print(i)
#     advanceOneGeneration(timers)
    #print(timers)

