vals = [[int(x) for x in line] for line in open("15.txt").read().splitlines()]
costs = [[0] * 500 for dummy in range(500)]
queue = [[(0, 0)]] + [[] for dummy in range(10000)]
v = 0
while costs[499][499] == 0:
    for (y, x) in queue[v]:
        if v > costs[y][x]:
            continue
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if y+dy >= 0 and y+dy < 500 and x+dx >= 0 and x+dx < 500:
                dt = ((vals[(y+dy) % 100][(x+dx) % 100] +
                      (y+dy)//100 + (x+dx)//100 - 1) % 9)+1
                if costs[y+dy][x+dx] == 0:
                    costs[y+dy][x+dx] = v + dt
                    queue[v+dt].append((y+dy, x+dx))
    v += 1
print(costs[499][499])
