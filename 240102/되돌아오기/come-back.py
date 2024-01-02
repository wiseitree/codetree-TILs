import sys
n = int(input())

x, y = 0, 0
dxs, dys = [0, 1, -1, 0], [-1, 0, 0, 1]
mapper = {
    'W' : 0,
    'S' : 1,
    'N' : 2,
    'E' : 3
}

querys = [
    tuple(input().split())
    for _ in range(n)
]

elapsed_time = 0

for d, dist in querys:
    curr_dir = mapper[d]

    for _ in range(int(dist)):
        x, y = x + dxs[curr_dir], y + dys[curr_dir]
        elapsed_time += 1
        if (x, y) == (0, 0):
            print(elapsed_time)
            sys.exit()

print(-1)