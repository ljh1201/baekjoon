# %%
# q1
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
_max = 0

for n1 in range(len(num_list)):
    for n2 in range(n1+1, len(num_list)):
        for n3 in range(n2+1, len(num_list)):
            _sum = num_list[n1] + num_list[n2] + num_list[n3]
            if _sum <= M and _sum > _max:
                _max = _sum

print(_max)

# %%
# q2
N = int(input())
result = N

for n in range(N, 1, -1):
    m = list(map(int, str(n)))
    if n + sum(m) == N:
        result = n

print(result if result != N else '0')

# %%
# q3
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)

# %%
# q4
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer1 = [['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B']]
answer2 = answer1[::-1]
answer_list = []

for x in range(0, N-7):
    for y in range(0, M-7):
        cnt1 = 0
        cnt2 = 0
        check_list = []
        for z in range(x, x+8):
            check_list.append(board[z][y:y+8])

        for i in range(8):
            for j in range(8):
                if answer1[i][j] != check_list[i][j]:
                    cnt1 += 1
                if answer2[i][j] != check_list[i][j]:
                    cnt2 += 1
                
        answer_list.append(min(cnt1, cnt2))

print(min(answer_list))

# %%
# q5
N = int(input())
answer = []
num = 0
while len(answer) < N:
    num += 1
    if '666' in str(num):
        answer.append(num)

print(answer[-1])

# %%
# q6
N = int(input())
loop = N
result = []
for i in range(loop):
    for j in range(loop):
        if N == 5 * i + 3 * j:
            result.append(i+j)

print(min(result) if len(result) > 0 else -1)
