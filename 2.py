f = open("2.txt", "r")
lines = f.readlines()

x = 0
y = 0
aim = 0

for line in lines:
    tokens = line.split()
    assert(len(tokens) == 2)
    
    dir = tokens[0]
    val = int(tokens[1])
    
    if (dir == "forward"):
        x += val
        y += aim * val
    elif (dir == "down"):
        aim += val
    elif (dir == "up"):
        aim -= val
    else:
        assert(false)

print(x)
print(y)
print(x * y)
    