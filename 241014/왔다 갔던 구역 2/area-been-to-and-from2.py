# queries = []
# n = int(input())

# blocks = [0]*2001
# current_x = 1000
# for _ in range(n):
#     x, type = input().split()
#     queries.append((int(x), type))


# def draw_blocks(x, type):
#     global current_x
    
#     if type == 'L':
#         left_x = current_x - x
#         right_x = current_x
    
#     if type == 'R':
#         left_x = current_x
#         right_x = current_x + x
    
#     for i in range(left_x, right_x):
#         blocks[i] += 1
    
    
# for x, type in queries:
#     draw_blocks(x, type)

# sum_val = 0
# for i in range(0, 2001):
#     if blocks[i] >= 2:
#         sum_val += 1

# print(sum_val)

offset = 1000
blocks = [0] * 2001
queries = []
n = int(input())
cur_x = 1000

for _ in range(n):
    x, d = input().split()
    queries.append((int(x), d))


def draw_block(x, d):
    global cur_x

    if d == 'R':
        x1 = cur_x
        x2 = cur_x + x
        cur_x = cur_x + x

    if d == 'L':
        x1 = cur_x - x
        x2 = cur_x
        cur_x = cur_x - x

    for i in range(x1, x2):
        blocks[i] += 1


for x, d in queries:
    draw_block(x, d)

ans = 0
for b in blocks:
    if b >= 2:
        ans += 1

print(ans)