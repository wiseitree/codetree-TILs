n = int(input())
grid = [
    input()
    for _ in range(n)
]
k = int(input())
ans = 0

def init(k):
    if k <= n:
        return 0, k-1, 0
    elif k <= 2*n:
        return k - n - 1, n - 1, 1
    elif k <= 3*n:
        return n-1, n - (k - 2*n), 2
    else:
        return n - (k - 3*n), 0, 3
    

def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def simulate(x, y, curr_dir):
    global ans
 
    while in_range(x, y):
        if grid[x][y] == '/':
            x, y, curr_dir = move(x, y, curr_dir ^ 1)
        else:
            x, y, curr_dir = move(x, y, 3 - curr_dir)

        ans += 1
    

x, y, curr_dir = init(k)
simulate(x, y, curr_dir)
print(ans)