# %%
# q1
N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')

# %%
# q2
T = int(input())
A = []
B = []

for i in range(T):
    a, b = map(int, input().split())
    A.append(a), B.append(b)

for j in range(T):
    print(A[j] + B[j])

# %%
# q3
n = int(input())
result = 0

for i in range(1, n+1):
    result += i
print(result)

# %%
# q4
X = int(input())
N = int(input())
sum = 0

for i in range(N):
    price = list(map(int, input().split()))
    sum += price[0] * price[1]
print('Yes' if sum == X else 'No')

# %%
# q5
N = int(input())
print('long ' * (N//4), end = ''), print('int')

# %%
# q6
import sys

T = int(input())

for i in range(T):
    A, B = (map(int, sys.stdin.readline().split()))
    print(A + B)

# %%
# q7
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')

# %%
# q8
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')

# %%
# q9
N = int(input())

for i in range(1, N+1):
    print('*'*i)

# %%
# q10
N = int(input())

for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)

# %%
# q11
loop = True
sum = []
while loop:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        loop = False
    else:
        sum.append(a + b)

for i in range(len(sum)):
    print(sum[i])

# %%
# q12
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break