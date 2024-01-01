n, m = tuple(map(int, input().split()))
grid = [
    [0] * n
    for _ in range(n)
]
checked = [
    [False] * n
    for _ in range(n)
]

querys = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def comfortable(x, y):
    return in_range(x, y) and grid[x][y] == 1
    

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
for r, c in querys:
    x, y = r-1, c-1
    grid[x][y] = 1
    cnt = 0
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if comfortable(nx, ny):
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)