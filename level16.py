# %%
# q1
N = int(input())
print(N * (N-1) if N > 1 else '0')

# %%
# q2
N = int(input())
print(2 ** N)

# %%
# q3
N = int(input())
result = 1
for i in range(1, N+1):
    result *= i
print(result)

# %%
# q4
import math
n, k = map(int, input().split())
print(int(math.factorial(n) / (math.factorial(k)*math.factorial(n-k))))

# %%
# q5
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    if n == m:
        print(1)
    elif n == 1:
        print(m)
    else:
        total = 1
        for i in range(n):
            total *= (m-i)
            total //= 1 + i
        print(total)
