# %%
# q1
N = int(input())

num_list = list(map(int, input().split()))

V = int(input())
print(num_list.count(V))

# %%
# q2
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end = ' ')

# %%
# q3
N = int(input())
_list = list(map(int, input().split()))
print(min(_list), max(_list))

# %%
# q4
num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = max(num_list)
max_index = num_list.index(max_num) + 1

print(max_num)
print(max_index)

# %%
# q5
N, M = map(int, input().split())
N_list = [0 for n in range(N)]
M_list = []

for loop in range(M):
    M_list.append(list(map(int, input().split())))

for i, j, k in M_list:
    N_list[i-1:j] = [k for m in range(len(N_list[i-1:j]))]
    
for p in N_list: 
    print(p, end = ' ')

# %%
# q6
N, M = map(int, input().split())
N_list = [n for n in range(1, N+1)]
M_list = [list(map(int, input().split())) for _ in range(M)]

for m in M_list:
    N_list[m[0]-1], N_list[m[1]-1] = N_list[m[1]-1], N_list[m[0]-1]

for p in N_list: 
    print(p, end = ' ')

# %%
# q7
n = [int(input()) for _ in range(28)]

for i in range(1, 31):
    if i in n:
        continue
    else:
        print(i)

# %%
# q8
n = [int(input()) for _ in range(10)]
remain = []

for i in n:
    if i % 42 in remain:
        continue
    else:
        remain.append(i % 42)

print(len(remain))

# %%
# q9
N, M = map(int, input().split())
N_list = [n for n in range(1, N+1)]
M_list = [list(map(int, input().split())) for _ in range(M)]

for m in M_list:
    N_list[m[0]-1:m[1]] = N_list[m[1]-N-1:m[0]-N-2:-1]

for p in N_list: 
    print(p, end = ' ')

# %%
# q10
subject = int(input())
score = list(map(int, input().split()))

max_score = max(score)
for i in range(len(score)):
    score[i] = score[i] / max_score * 100

print(sum(score) / len(score))
