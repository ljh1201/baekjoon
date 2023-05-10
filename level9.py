# %%
# q1
result = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    result.append('multiple' if A % B == 0 else 'factor' if B % A == 0 else 'neither')
for i in result:
    print(i)

# %%
# q2
N, K = map(int, input().split())
N_list = []
for i in range(1, N+1):
    if N % i == 0:
        N_list.append(i)
try:
    print(N_list[K-1])
except:
    print(0)

# %%
# q3
result = []
while True:
    n = int(input())
    n_list = []
    if n == -1:
        break
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)

    result.append(n_list)

for rst in result:
    if rst[-1] == sum(rst[:-1]):
        print(f'{rst[-1]} = {rst[0]}', end='')
        for r in rst[1:-1]:
            print(f' + {r}', end='')
        print()
    else:
        print(f'{rst[-1]} is NOT perfect.')

# %%
# q4
N = int(input())
N_list = list(map(int, input().split()))
cnt = 0
result = 0

for n in N_list:
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        result += 1
    cnt = 0

print(result)

# %%
# q5
M = int(input())
N = int(input())
_sum = 0
_min = N+1
cnt = 0
for n in range(M, N+1):
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        _sum += n
        if _min > n:
            _min = n
    cnt = 0
if _sum == 0:
    print(-1)
else:
    print(_sum)
    print(_min)

# %%
# q6
N = int(input())
i = 2
primes = []
while i * i <= N:
    while (N % i) == 0:
        N //= i
        print(i)
    i += 1
if N > 1:
    print(n)
