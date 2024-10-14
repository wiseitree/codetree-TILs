max_t = 1000
pos_at_time_a = [0] * (max_t + 1)
pos_at_time_b = [0] * (max_t + 1)
n, m = tuple(map(int, input().split()))
cur_pos_a = 0
cur_pos_b = 0
cur_time_a = 0
cur_time_b = 0


def move(d, t, cur_time,pos_at_time):
    step = 1 if d == 'R' else -1

    for _ in range(t):
        cur_time += 1
        pos_at_time[cur_time] = pos_at_time[cur_time-1] + step

    return cur_time


for _ in range(n):
    d, t = input().split()
    cur_time_a = move(d, int(t), cur_time_a, pos_at_time_a)

for _ in range(m):
    d, t = input().split()
    cur_time_b = move(d, int(t), cur_time_b, pos_at_time_b)

ans = -1
for t in range(1, 1001):
    if pos_at_time_a[t] == pos_at_time_b[t]:
        ans = t
        break

print(ans)